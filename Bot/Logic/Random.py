from Bot.Logic.Algorithms import AlgorithmBase
import chess


class RandomBot:
    def __init__(self, state=None):
        self._base = AlgorithmBase(state)
