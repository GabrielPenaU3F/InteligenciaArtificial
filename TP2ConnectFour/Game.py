from InteligenciaArtificial.TP2ConnectFour.TreeGenerator import TreeGenerator
from Players import *

from Board import Board


class Game():

    def __init__(self):

        self.board = Board()
        self.players = []
        self.tree_gen = TreeGenerator()


    def start(self, starter):

        if (starter == "F"):

            player1 = HumanPlayer('O', self)
            player2 = IAPlayer('X', self)
            self.players = [player1, player2]

        else:

            player1 = IAPlayer('O', self)
            player2 = HumanPlayer('O', self)
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

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def update_board(self, board):
        self.set_board(board)


