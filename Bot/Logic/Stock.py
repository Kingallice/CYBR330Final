from Bot.Logic.Base import AlgorithmBase
import chess
import requests

class StockFish(AlgorithmBase):

    def getMove(self):
        return self.getStockFishSuggestions()[0]['uci']

    def getStockFishSuggestions(self):
        url = 'https://tablebase.lichess.ovh/standard?fen='+ self.getBoard().fen()
        req = requests.get(url).json()['moves']
        return req