import random

from Bot.Logic.Base import AlgorithmBase
import chess


class DumbBot(AlgorithmBase):

    def getMove(self):
        # I don't know if i need this

        moveHistory = []
        legalcaptures = []
        board = self.getBoard()
        legal_Moves = board.generate_legal_moves()

        # need to move pawns at c7,d7,e7,f7 forwards 2 then moves them all forward one if applicable
        if chess.Board().piece_at(chess.C7):
            chess.Move.from_uci('c7c5').uci()
        elif chess.Board().piece_at(chess.D7):
            chess.Move.from_uci('d7d5').uci()
        elif chess.Board().piece_at(chess.E7):
            chess.Move.from_uci('e7e5').uci()
        elif chess.Board().piece_at(chess.F7):
            chess.Move.from_uci('f7f5').uci()
        elif chess.Board().piece_at(chess.C5):
            chess.Move.from_uci('c5c4').uci()
        elif chess.Board().piece_at(chess.D5):
            chess.Move.from_uci('d5d4').uci()
        elif chess.Board().piece_at(chess.E5):
            chess.Move.from_uci('e5e4').uci()
        elif chess.Board().piece_at(chess.F5):
            chess.Move.from_uci('f5f4').uci()

        # implementing random moves for when logic is not applicable for above
        for moves in legal_Moves:
            board = self.getBoard()
            board.push_uci(moves.uci())
            moves = random.choice(list(board.generate_legal_moves()))
            return moves.uci()

        # attempting a optimized route

    def getName(self):
        return "Dumb Bot"


# -------------Test Code for Move Choice--------------------#
d = DumbBot()
print(d.getMove())
print(d.getName())
