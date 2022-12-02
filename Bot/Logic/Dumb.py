import random

from Bot.Logic.Base import AlgorithmBase
import chess


class DumbBot(AlgorithmBase):

    # so far only works for black
    def getMove(self):

        moveHistory = []
        board = self.getBoard()
        legal_Moves = [move.uci() for move in self.getBoard().generate_legal_moves()]
        move_List = ['c7c5', 'd7d5', 'e7e5', 'f7f5','b7b5','g7g5','a7a5','h7h5','c2c4','d2d4','e2e4','f2f4'
                     'b2b4','g2g4','a2a4']
        for x in move_List:
            if x in legal_Moves and self.getBoard().piece_at(chess.Move.from_uci(x).from_square).piece_type == 1:
                return x

        for i in legal_Moves:
            if i in legal_Moves and self.getBoard().piece_at(chess.Move.from_uci(i).from_square).piece_type == 1:
                return i
        # for x in move_List:
        #     if x in legal_Moves and self.getBoard().piece_at(chess.Move.from_uci(x).from_square).piece_type == 1:
        #         return x
        # need to move pawns at c7,d7,e7,f7 forwards 2 then moves them all forward one if applicable
        # if self.getBoard().piece_at(chess.C7):
        #     return chess.Move.from_uci('c7c5').uci()
        # if self.getBoard().piece_at(chess.D7):
        #     return chess.Move.from_uci('d7d5').uci()
        # if self.getBoard().piece_at(chess.E7):
        #     return chess.Move.from_uci('e7e5').uci()
        # if self.getBoard().piece_at(chess.F7):
        #     return chess.Move.from_uci('f7f5').uci()
        # if self.getBoard().piece_at(chess.C5):
        #     return chess.Move.from_uci('c5c4').uci()
        # if self.getBoard().piece_at(chess.D5):
        #     return chess.Move.from_uci('d5d4').uci()
        # if self.getBoard().piece_at(chess.E5):
        #     return chess.Move.from_uci('e5e4').uci()
        # if self.getBoard().piece_at(chess.F5):
        #     return chess.Move.from_uci('f5f4').uci()

        # implementing random moves for when logic is not applicable for above
        print([move.uci() for move in self.getBoard().generate_legal_moves()])
        return random.choice([move.uci() for move in self.getBoard().generate_legal_moves()])

    def getName(self):
        return "Dumb Bot"

# -------------Test Code for Move Choice--------------------#
# d = DumbBot()
# print(d.getMove())
# print(d.getName())
