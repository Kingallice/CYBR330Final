import random

from Bot.Logic.Base import AlgorithmBase
import chess


class DumbBot(AlgorithmBase):

    # this is basically a pawn blitzkrieg
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

        # implementing random moves for when logic is not applicable for above
        print([move.uci() for move in self.getBoard().generate_legal_moves()])
        return random.choice([move.uci() for move in self.getBoard().generate_legal_moves()])

    def getName(self):
        return "Dumb Bot"




# -------------Test Code for Move Choice--------------------#
# put the code below in main to test, change the user name based on whos being challenged
# bot = ChessBot()
# ChallengeUtil.acceptChallenges(bot, [DumbBot, KillBot, RandomBot, BestBot, StockFish])
# ChallengeUtil.sendChallenge(bot, {"username": "chessgarret"})
