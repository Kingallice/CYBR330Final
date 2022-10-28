import Algorithms
import chess


class StockFish:
    def __int__(self, state=None):
        self._base = Algorithms(state)

    def moveUCI(self, e):
        """Adds a move using UCI (ex: e2e4 - StartEnd) format to the board"""
        self._board.push(chess.Move.from_uci(e))

    def color(self):
        """Returns the color of the current player."""
        if self._board.turn:
            return "White"
        return "Black"

    def isTurn(self, color):
        """Returns True if color is for current player"""
        return self.color().lower() == color.lower()