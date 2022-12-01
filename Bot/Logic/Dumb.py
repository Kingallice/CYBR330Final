from Bot.Logic.Base import AlgorithmBase
import chess


class DumbBot(AlgorithmBase):

    def getMove(self):
        # idk if i need this
        legalmoves = []
        legalcaptures = []
        board = self.getBoard()

    def wallBreaker(self):

        board = self.getBoard()
        if DumbBot.color() is "White":
            # move the three pawns at c2,d2,e2 to c4,d4,e4
            # this leaves the king open
            #if board.
            pass

        # move pawns first then once pawns are gone then randomly move queen then move king straight forward
        #else:
