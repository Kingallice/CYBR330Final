from re import X
import chess


class AlgorithmBase():
    """Base class for chess"""

    def __init__(self, state=None):
        """Initializes a chess Board (if state is passed it will intialize based on state)"""
        self._board = chess.Board()
        if state is not None:
            for x in state.split(' '):
                self._board.push(chess.Move.from_uci(x))

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

    def getBoard(self):
        """Returns a copy of the board"""
        return self._board.copy()