from Bot.Logic.Base import AlgorithmBase
import chess


class KillBot:
    def __init__(self, state=None):
        self._base = AlgorithmBase(state)

