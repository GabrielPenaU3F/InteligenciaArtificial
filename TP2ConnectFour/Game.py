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

        finished = False
        while not finished:
            for player in self.players:
                player.move()
                if (self.finished() == True):
                    finished = True
                    break


    def finished(self):

        for player in self.players:
            if (player.won):
                return True

        return False

