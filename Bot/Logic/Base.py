import chess


class AlgorithmBase:
    """Base class for chess"""

    def __init__(self, state=None):
        """Initializes a chess Board (if state is passed it will initialize based on state)"""
        self._board = chess.Board()
        if state is not None:
            for x in state.split(' '):
                if x == '':
                    break
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

    def copy(self):
        """Returns a copy of the algorithm"""
        return self(self.getBoard())

    def getPieceCount(self, board=None, color=""):
        """Returns dictionary of pieces remaining for each color (or specified color only)."""
        white = {}
        black = {}
        if not board:
            board = self._board
        for x in board.board_fen():
            if x.islower():
                if x in black.keys():
                    black[x] += 1
                else:
                    black[x] = 1
            elif x.isupper():
                if x in white.keys():
                    white[x] += 1
                else:
                    white[x] = 1
        if color.lower() == 'white':
            return white
        elif color.lower() == 'black':
            return black
        return {"white": white, "black": black}

    def getScores(self, board=None, color=""):
        """Returns score of each color (or color specified)."""
        scores = {"white": 0, "black": 0}
        if board:
            pieces = self.getPieceCount(board)
        else:
            pieces = self.getPieceCount()
        for x in pieces:
            for y in pieces[x]:
                if y.lower() in ['p']:
                    scores[x] += 1 * pieces[x][y]
                elif y.lower() in ['k', 'b']:
                    scores[x] += 3 * pieces[x][y]
                elif y.lower() in ['r']:
                    scores[x] += 5 * pieces[x][y]
                elif y.lower() in ['q']:
                    scores[x] += 9 * pieces[x][y]
        if color.lower() == 'white':
            return scores['white']
        elif color.lower() == 'black':
            return scores['black']
        return scores

    def getName():
        """Abstract method to get the name of the Algorithm.
        
        Must be implemented by algorithm class!"""
        raise NotImplementedError("getName not Implemented")

    def getMove(self):
        """Abstract method to get a final move from the algorithm in UCI format.
        
        Must be implemented by algorithm class!"""
        raise NotImplementedError("getMove not Implemented")

