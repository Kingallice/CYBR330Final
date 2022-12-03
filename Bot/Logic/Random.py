from Bot.Logic.Base import AlgorithmBase
import chess
import random


class RandomBot(AlgorithmBase):
    """Subclass bot logic for a bot that chooses moves randomly"""
    def getName(self):
        return "Random"

    def getMove(self):
        """
        Chooses a move by selecting a random move from list of legal moves.
        :return: a UCI encoded chess move as a String
        """
        board = self.getBoard()
        return random.choice([move.uci() for move in board.generate_legal_moves()])


