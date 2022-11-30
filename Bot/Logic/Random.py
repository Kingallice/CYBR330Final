from Bot.Logic.Base import AlgorithmBase
import chess
import random


class RandomBot(AlgorithmBase):
    """Subclass bot logic for a bot that chooses moves randomly"""
    def getMove(self):
        """
        Chooses a move by selecting a random move from list of legal moves.
        :return: a UCI encoded chess move as a String
        """
        board = self.getBoard()
        move = random.choice(list(board.generate_legal_moves()))
        return move


