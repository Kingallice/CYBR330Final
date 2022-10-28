import Algorithms
import chess


class DumbBot(Algorithms):
    def __int__(self, state=None):
        self._board = chess.Board()
        if state is not None:
            for x in state.split(' '):
                self._board.push(chess.Move.from_uci(x))
