from Bot.Logic.Base import AlgorithmBase
from Bot.Logic.Stock import StockFish
import random

class KillBot(AlgorithmBase):

    def getName():
        return "Kill"
    
    def getMove(self):
        moves = [move.uci() for move in self.getBoard().generate_legal_captures()]
        if len(moves) > 0:
            return random.choice(moves)
        return StockFish(" ".join([move.uci() for  move in self.getBoard().move_stack])).getMove()
