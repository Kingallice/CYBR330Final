from Bot.Logic.Base import AlgorithmBase
import random
import requests


class BestBot(AlgorithmBase):
    """BestBot chooses the most beneficial move from the set of all available moves then plays that move."""

    def getName():
        """Returns a string representing this bots name (parameters left blank on purpose)"""
        return "Best"

    def copy(self):
        """Creates a copy of bot"""
        return BestBot(" ".join([move.uci() for move in self.getBoard().move_stack]))

    def rankState(self, bot):
        """Provides analysis of the current game state"""
        scores = self.getScores()
        if bot == "white":
            return scores['white'] - scores['black']
        return scores['black'] - scores['white']

    def minimax(self, bot, depth=0):
        """Implementation of Minimax search algorithm, iterates through possible moves scoring them,
        then utilizes the highest scoring move."""
        if depth > 2:
            return self.rankState(bot)
        moves, scores = [], []

        for move in self.getBoard().generate_legal_moves():
            temp = self.copy()
            temp.moveUCI(move.uci())
            scores.append(temp.minimax(bot, depth + 1))
            moves.append(move.uci())

        # print(moves, scores)

        if self.color() == bot:
            max_idx = scores.index(max(scores))
            move = moves[max_idx]
            self.moveUCI(move)
            return scores[max_idx]
        else:
            min_idx = scores.index(min(scores))
            move = moves[min_idx]
            self.moveUCI(move)
            return scores[min_idx]

    def getMove(self):
        """Method used to choose which move Best Bot will play using Minimax-like algorithm"""
        req = requests.get("https://explorer.lichess.ovh/masters?play=" + ",".join(
            [move.uci() for move in self.getBoard().move_stack]))
        openingList = req.json()["moves"]
        if openingList:
            return random.choice([move["uci"] for move in openingList])
        self.minimax(self.color())
        return self.getBoard().pop().uci()

    def getMoveX(self):
        """---------------DEPRECATED, use getMove()--------------------
        Method that serves the purpose of choosing the BestBot's next move"""
        board = self.getBoard()
        moves = board.generate_legal_moves()
        best_moves = []
        bot_color = self.color().lower()
        op_color = ''
        if bot_color == "white":
            op_color = "black"
        else:
            op_color = "white"

        for move in moves:
            board = self.getBoard()
            board.push_uci(move.uci())
            scores = self.getScores(board)

            if scores.get(bot_color) >= scores.get(op_color):
                best_moves.append(board.uci(move))

        if not best_moves:
            best_moves = [move.uci() for move in self.getBoard().generate_legal_moves()]
        if best_moves:
            c_index = random.randint(0, len(best_moves) - 1)
            move_choice = best_moves[c_index]
            return move_choice
        return ""
