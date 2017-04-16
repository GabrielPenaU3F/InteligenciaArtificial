from Players import *

from Board import Board


class Game():


    def start(self, starter):

        self.board = Board()
        if (starter == "F"):

            player1 = HumanPlayer('O', self.board)
            player2 = IAPlayer('X', self.board)
            self.players = [player1, player2]

        else:

            player1 = IAPlayer('O', self.board)
            player2 = HumanPlayer('O', self.board)
            self.players = [player1, player2]


        finished = False
        while not finished:
            for player in self.players:
                player.move()
                if (self.finished() == True):
                    finished = True
                    break

    # This can be done better. Redundant checks
    # because player 2 can't win in player 1's turn
    def finished(self):

        for player in self.players:
            if (player.won):
                return True

        return False

