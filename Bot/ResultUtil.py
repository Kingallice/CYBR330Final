from Bot.Intialization.Games import Game
import json

class ResultUtil:

    _resultPath="./results.txt"

    def resetResultFile():
        file = open(ResultUtil._resultPath, "w")
        file.write("")
        file.close()

    def getResultFile():
        try:
            file = open(ResultUtil._resultPath, "r")
            data = file.read()
            file.close()
            return json.loads(data)
        except:
            return None

    def saveResultFile(data):
        file = open(ResultUtil._resultPath, "w")
        file.save(json.dumps(data))
        file.close()

    def getWinLossDraw(data, opponent, algorithm):
        if data:
            if opponent in data.keys():
                if algorithm in data[opponent].keys():
                    temp = data[opponent][algorithm]
                    return (temp["win"], temp["loss"], temp["draw"])
        return (0, 0, 0)

    def saveResults(data, results):
        if data:
            data[results["Opponent"]][results["Algorithm"]] = {"win":results["Win"], "Loss":results["Loss"], "Draw":results["Draw"]}
        else:
            data = {results["Opponent"]:{results["Algorithm"]:{"win":results["Win"], "Loss":results["Loss"], "Draw":results["Draw"]}}}
        ResultUtil.saveResultFile(data)

    def formatResults(bot, game, endData, algorithm):
        botId = bot.getId()
        if endData == 'white' : 
            winner = game.getWhite() 
        elif endData == 'black' : 
            winner = game.getBlack()
        else :
            winner = None
        
        (win, loss, draw) = ResultUtil.getWinLossDraw(ResultUtil.getResultFile(), Game.getColorId(game.getOpponent(bot.getId())), algorithm.getName())

        if winner == None:
            print('Draw', {"Opponent" : Game.getColorId(game.getOpponent(bot.getId())), "Algorithm" : algorithm.getName(),  "Win" : win, "Loss": loss, "Draw" : draw+1})
        elif Game.getColorId(winner) == botId:
            print('We won', {"Opponent" : Game.getColorId(game.getOpponent(bot.getId())), "Algorithm" : algorithm.getName(),  "Win" : win+1, "Loss": loss, "Draw" : draw})
        else:
            print('We lost', {"Opponent" : Game.getColorId(game.getOpponent(bot.getId())), "Algorithm" : algorithm.getName(),  "Win" : win, "Loss": loss+1, "Draw" : draw})
        #print("Bot:", vars(bot), "\nGame:", vars(game), "\nWinner:", endData)