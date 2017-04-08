from Players import *

from Board import Board


class Game():


    def start(self, starter):

        self.board = Board()
        if (starter == "F"):

            player1 = HumanPlayer(self.board)
            player2 = IAPlayer(self.board)

        else:

            player1 = IAPlayer(self.board)
            player2 = HumanPlayer(self.board)

        self.players = [player1, player2]

        while self.not_finished():
            for player in self.players:
                player.move()


    def not_finished(self):

        if self.board.has_a_line_of_four():
            return False

        else: return True

