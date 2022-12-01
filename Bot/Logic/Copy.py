from Bot.Logic.Base import AlgorithmBase
import chess


class CopyBot(AlgorithmBase):
    """CopyBot chooses its move based on it's opponents last move. In essence, it copies the move of the opponent
    when possible, and moves at random when a copy is not possible."""
    def getMove(self):
        """Class method that serves the purpose of choosing the CopyBot's next move. Move choice is copying the
        opponent's move preferably. Randomly chooses a move if copy is not possible."""


