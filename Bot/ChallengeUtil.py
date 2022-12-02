from Bot.GameConnector import GameConnector
import time
import random
import requests
import threading
LiChessAPI = "https://lichess.org/api/challenge"

class ChallengeUtil:

    def acceptChallenges(bot, algoList):
        timer = time.time()
        while True:
            if time.time() - timer > 60:
                req = requests.get(LiChessAPI, headers={"Authorization":'Bearer ' + bot.getKey()}).json()
                if req['in']:
                    for chal in req['in']:
                        requests.post(LiChessAPI+'/'+chal['id']+'/accept', headers={"Authorization":'Bearer ' + bot.getKey()})
                        threading.Thread(target=GameConnector, args=(bot, chal['id'], random.choice(algoList))).start()

    def startAcceptingChallenges(bot, algoList):
        threading.Thread(target=ChallengeUtil.acceptChallenges, args=(bot, algoList))

    def sendChallenge(bot, opponent):
        if "username" in opponent.keys():
            data = None
            if opponent["username"] == 'ai' and "level" in opponent.keys():
                data = {'level': opponent['level']}
            info = requests.post(LiChessAPI+'/'+opponent["username"], data=data, headers={"Authorization" : 'Bearer ' + bot.getKey()})
            return(info.json()["id"])
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
            for challenge in challenges:
                newThread = threading.Thread(target=GameConnector, args=(bot, challenge, algo))
                newThread.start()
            while threading.activeCount() > 1:
                pass