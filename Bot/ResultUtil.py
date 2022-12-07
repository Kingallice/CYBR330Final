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
        file.write(json.dumps(data))
        file.close()

    def getWinLossDraw(data, opponent, algorithm):
        if data:
            if opponent in data.keys():
                if algorithm.getName() in data[opponent].keys():
                    temp = data[opponent][algorithm.getName()]
                    return (temp["Win"], temp["Loss"], temp["Draw"], temp["MoveAvg"])
        return (0, 0, 0, 0)

    def saveResults(data, results):
        if data:
            if results["Opponent"] in data.keys():
                data[results["Opponent"]][results["Algorithm"]] = {"Win":results["Win"], "Loss":results["Loss"], "Draw":results["Draw"], "MoveAvg":results["MoveAvg"]}
            else:
                data[results["Opponent"]] = {results["Algorithm"]: {"Win":results["Win"], "Loss":results["Loss"], "Draw":results["Draw"], "MoveAvg":results["MoveAvg"]}}
        else:
            data = {results["Opponent"]:{results["Algorithm"]:{"Win":results["Win"], "Loss":results["Loss"], "Draw":results["Draw"], "MoveAvg":results["MoveAvg"]}}}
        ResultUtil.saveResultFile(data)

    def formatResults(bot, game, moves, endData, algorithm):
        botId = bot.getId()
        if endData == 'white' : 
            winner = game.getWhite() 
        elif endData == 'black' : 
            winner = game.getBlack()
        else :
            winner = None
        
        (win, loss, draw, moveAvg) = ResultUtil.getWinLossDraw(ResultUtil.getResultFile(), Game.getColorId(game.getOpponent(bot.getId())), algorithm)
        moveAvg = moveAvg*(win+loss+draw)

        if winner == None:
            ResultUtil.saveResults(ResultUtil.getResultFile(), {"Opponent" : Game.getColorId(game.getOpponent(bot.getId())), "Algorithm" : algorithm.getName(),  "Win" : win, "Loss": loss, "Draw" : draw+1, "MoveAvg": (moveAvg+moves)/(win+loss+draw+1)})
        elif Game.getColorId(winner) == botId:
            ResultUtil.saveResults(ResultUtil.getResultFile(), {"Opponent" : Game.getColorId(game.getOpponent(bot.getId())), "Algorithm" : algorithm.getName(),  "Win" : win+1, "Loss": loss, "Draw" : draw, "MoveAvg": (moveAvg+moves)/(win+loss+draw+1)})
        else:
            ResultUtil.saveResults(ResultUtil.getResultFile(), {"Opponent" : Game.getColorId(game.getOpponent(bot.getId())), "Algorithm" : algorithm.getName(),  "Win" : win, "Loss": loss+1, "Draw" : draw, "MoveAvg": (moveAvg+moves)/(win+loss+draw+1)})
        #print("Bot:", vars(bot), "\nGame:", vars(game), "\nWinner:", endData)