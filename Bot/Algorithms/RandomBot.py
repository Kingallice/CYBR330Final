from Bot.Algorithms import Algorithms
import chess


class RandomBot:
    def __init__(self, state=None):
        self._base = Algorithms(state)
