from Bot.GameConnector import GameConnector
import requests
import threading
LiChessAPI = "https://lichess.org/api/challenge/"

class ChallengeUtil:

    def sendChallenge(bot, opponent):
        if "username" in opponent.keys():
            data = None
            if opponent["username"] == 'ai' and "level" in opponent.keys():
                data = {'level': opponent['level']}
            info = requests.post(LiChessAPI+opponent["username"], data=data, headers={"Authorization" : 'Bearer ' + bot.getKey()})
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
            print(opponent)
            challenges = ChallengeUtil.createChallenges(bot, opponent, num)
            print(challenges)
            for challenge in challenges:
                newThread = threading.Thread(target=GameConnector, args=(bot, challenge, algo))
                newThread.start()
            print(threading.activeCount())
            while threading.activeCount() > 0:
                pass