from Bot.Intialization.Games import Game

import json
import requests

url="https://lichess.org/api/bot/game"

class GameConnector:
    """Connects the program to the lichess api for playing the passed game utilizing passed algorithm."""

    def __init__(self, bot, gameId, algorithm):
        self._bot = bot
        self._game = None
        self._algo = algorithm
        self._intializeAlgorithm(gameId)
        
    def sendMove(self, move):
        req = requests.post(url+'/'+self._game.getGameId()+'/move/'+move, headers={"Authorization":'Bearer ' + self._bot.getKey()})

    def _intializeAlgorithm(self, gameId):
        req = requests.get(url+'/stream/'+gameId, headers={"Authorization":'Bearer ' + self._bot.getKey()}, stream=True)

        if req.status_code == 200:
            for line in req.iter_lines():
                if line:
                    lineData = json.loads(line.decode('utf-8'))
                    if 'winner' in lineData.keys():
                        if lineData['winner'] == 'white':
                            print('Game End:',Game.getColorName(self._game.getWhite()),'is victorious!')
                        else: 
                            print('Game End:',Game.getColorName(self._game.getBlack()),'is victorious!')
                        break
                    if 'status' in lineData.keys() and lineData['status'] == 'draw':
                        print('Game End: Draw')
                        break
                    if 'state' in lineData.keys():
                        self._game = Game(lineData)
                        lineData = lineData['state']
                    if 'moves' in lineData.keys():
                        if (len(lineData['moves'].split(' ')) % 2 == 0 or lineData['moves'] == '') and self._game.getColor(self._bot.getId()) == 'white':
                            algo = self._algo(lineData['moves'])
                            self.sendMove(algo.getMove())
                        elif len(lineData['moves'].split(' ')) % 2 == 1 and self._game.getColor(self._bot.getId()) == 'black':
                            algo = self._algo(lineData['moves'])
                            self.sendMove(algo.getMove())
        req.close()