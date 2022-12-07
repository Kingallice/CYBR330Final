from Bot.GameConnector import GameConnector
import time
import random
import requests
import threading
import json
LiChessAPI = "https://lichess.org/api/challenge"

class ChallengeUtil:

    def resumeGames(bot, algoList):
        req = requests.get("https://lichess.org/api/account/playing", headers={"Authorization":'Bearer ' + bot.getKey()}).json()
        for chal in req['nowPlaying']:
            while threading.active_count() > 5:
                continue
            threading.Thread(target=GameConnector, args=(bot, chal['gameId'], random.choice(algoList))).start()

    def acceptChallenges(bot, algoList):
        timer = None
        while True:
            if not timer or time.time() - timer > 60:
                req = requests.get(LiChessAPI, headers={"Authorization":'Bearer ' + bot.getKey()}).json()
                if req['in']:
                    for chal in req['in']:
                        while threading.active_count() > 5:
                            continue
                        requests.post(LiChessAPI+'/'+chal['id']+'/accept', headers={"Authorization":'Bearer ' + bot.getKey()})
                        threading.Thread(target=GameConnector, args=(bot, chal['id'], random.choice(algoList))).start()
                timer = time.time()

    def startAcceptingChallenges(bot, algoList):
        threading.Thread(target=ChallengeUtil.acceptChallenges, args=(bot, algoList),name="Accepting Challenges").start()

    def sendChallenge(bot, opponent):
        if "username" in opponent.keys():
            data = None
            if opponent["username"] == 'ai' and "level" in opponent.keys():
                data = {'level': opponent['level']}
            req = requests.post(LiChessAPI+'/'+opponent["username"], data=data, headers={"Authorization" : 'Bearer ' + bot.getKey()}, stream=True)
            try:
                for line in req.iter_lines():
                    if line and line != "":
                        line = json.loads(line.decode('utf-8'))
                        if "challenge" in line.keys():
                            line = line["challenge"]
                            if line["status"] == "created":
                                return line["id"]
                        if "source" in line.keys():
                            if line["source"] == "ai":
                                return line["id"]
            except:
                return None
        return None
    
    def createChallenges(bot, opponent, num):
        challenges = []
        for i in range(num):
            challenge = ChallengeUtil.sendChallenge(bot, opponent)
            if challenge:
                challenges.append(challenge)
        return challenges

    def testAlgorithm(bot, algo, opponentList, num):
        for opponent in opponentList:
            i = 0
            while i < num: 
                while threading.active_count() > 5:
                    continue
                challenge = ChallengeUtil.sendChallenge(bot, opponent)
                i += 1
                threading.Thread(target=GameConnector, args=(bot, challenge, algo), name="Game " + str(i) + " " + str(opponent) + " - " + algo.getName()).start()