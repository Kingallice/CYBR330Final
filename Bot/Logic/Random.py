from Bot.Logic.Base import AlgorithmBase
import chess
import random


class RandomBot(AlgorithmBase):

    def getMove(self):
        """"""
        board = self.getBoard()
        move = random.choice(list(board.generate_legal_moves()))
        return move


