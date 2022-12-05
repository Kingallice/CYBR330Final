from Bot.GameConnector import GameConnector
import time
import random
import requests
import threading
LiChessAPI = "https://lichess.org/api/challenge"

class ChallengeUtil:

    def acceptChallenges(bot, algoList):
        timer = None
        while True:
            if not timer or time.time() - timer > 60:
                req = requests.get(LiChessAPI, headers={"Authorization":'Bearer ' + bot.getKey()}).json()
                if req['in']:
                    for chal in req['in']:
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
            req = requests.post(LiChessAPI+'/'+opponent["username"], data=data, headers={"Authorization" : 'Bearer ' + bot.getKey()})
            info = req.json()
            if "challenge" in info.keys():
                info = info["challenge"]
            return(info["id"])
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
            challenges = ChallengeUtil.createChallenges(bot, opponent, num)
            i = 0
            for challenge in challenges:
                while threading.activeCount() > 5:
                    time.sleep(60)
                i += 1
                newThread = threading.Thread(target=GameConnector, args=(bot, challenge, algo), name="Game " + str(i) + " " + str(opponent) + " - " + algo.getName())
                newThread.start()