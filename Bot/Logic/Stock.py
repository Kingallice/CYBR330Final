from Bot.Logic.Base import AlgorithmBase
import chess
import requests

class StockFish(AlgorithmBase):

    def getMove(self):
        try:
            return self.getStockFishSuggestions()[0]
        except:
            return None

    def getStockFishSuggestions(self):
        url = 'https://lichess.org/api/cloud-eval?fen='+ self.getBoard().fen()
        req = requests.get(url)
        if req.status_code == 200:
            return req.json()['pvs'][0]['moves'].split(' ')
        else:
            url = 'https://tablebase.lichess.ovh/standard?fen='+ self.getBoard().fen()
            req = requests.get(url).json()['moves']
            movesList = []
            for move in req:
                movesList.append(move['uci'])
            return movesList