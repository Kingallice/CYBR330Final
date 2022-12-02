from Bot.Logic.Base import AlgorithmBase
import chess


class DumbBot(AlgorithmBase):

    def getMove(self):
        # idk if i need this
        legalmoves = []
        moveHistory = []
        legalcaptures = []
        board = self.getBoard()

    def wallBreaker(self):

        board = self.getBoard()
        legal_Moves = board.legal_moves
        # need to move pawns at c7,d7,e7,f7 forwards 2
        if chess.Board().piece_at(chess.C7):
            chess.Move.from_uci('c7c5')
        elif chess.Board().piece_at(chess.D7):
            chess.Move.from_uci('d7d9')
        elif chess.Board().piece_at(chess.E7):
            chess.Move.from_uci('e7e9')
        elif chess.Board().piece_at(chess.F7):
            chess.Move.from_uci('f7f9')


                # or (chess.Board().piece_at(chess.D7) or chess.Board().piece_at(chess.E7) or chess.Board().piece_at(chess.F7)):




        # chess.Move.from_uci(" ") in legal_Moves

        # move the three pawns at c2,d2,e2 to c4,d4,e4
        # this leaves the king open
        # move pawns first then once pawns are gone or no legal moves left then move remaining pieces forwards as far as available
        # else: