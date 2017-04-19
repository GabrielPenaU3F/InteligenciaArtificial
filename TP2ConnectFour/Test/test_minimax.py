import unittest

from InteligenciaArtificial.TP2ConnectFour.Board import Board
from InteligenciaArtificial.TP2ConnectFour.Game import Game
from InteligenciaArtificial.TP2ConnectFour.Players import *


class MinimaxTest(unittest.TestCase):

    def test_evaluating_function_gives_correct_value(self):

        board = Board()

        board.grid[5][0] = '$'
        board.grid[5][1] = '$'
        board.grid[5][3] = 'O'
        board.grid[5][4] = 'O'
        board.grid[5][5] = 'O'
        board.grid[4][3] = '$'
        board.grid[4][4] = 'O'
        board.grid[4][5] = 'O'
        board.grid[3][4] = '$'
        board.grid[3][5] = 'O'
        board.grid[2][5] = '$'

        board.print_grid()

        self.assertEquals(1100, board.evaluate_value('O'))


    #TODO: Test the minimax tree

        """
        game = Game()
        player1 = HumanPlayer('O', game)
        player2 = IAPlayer('X', game)
        game.players.append(player1)
        game.players.append(player2)
        """





    if __name__ == '__main__':
        unittest.main()