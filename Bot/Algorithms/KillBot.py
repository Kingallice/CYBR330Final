from Bot.Algorithms import Algorithms
import chess


class KillBot:
    def __init__(self, state=None):
        self._base = Algorithms(state)

