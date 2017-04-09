import unittest

import sys

from InteligenciaArtificial.TP2ConnectFour.Board import Board


class BoardTest(unittest.TestCase):

    def test_do_not_find_vertical_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_vertical())


    def test_do_not_find_horizontal_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_horizontal())


    def test_do_not_find_positive_diagonal_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_positive_slopes())


    def test_do_not_find_negative_diagonal_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_negative_slopes())


    def test_find_vertical_c4(self):

        board = Board()
        board.grid[1][2] = 'O'
        board.grid[2][2] = 'O'
        board.grid[3][2] = 'O'
        board.grid[4][2] = 'O'

        board.print_grid()

        self.assertTrue(board.look_for_4_vertical())


    def test_find_horizontal_c4(self):

        board = Board()
        board.grid[3][3] = 'X'
        board.grid[3][4] = 'X'
        board.grid[3][5] = 'X'
        board.grid[3][6] = 'X'

        board.print_grid()

        self.assertTrue(board.look_for_4_horizontal())


    def test_find_negative_diagonal_c4(self):

        board = Board()
        board.grid[1][1] = 'X'
        board.grid[2][2] = 'X'
        board.grid[3][3] = 'X'
        board.grid[4][4] = 'X'

        board.print_grid()

        self.assertTrue(board.look_for_4_negative_slopes())


    def test_find_positive_diagonal_c4(self):

        board = Board()
        board.grid[4][1] = 'X'
        board.grid[3][2] = 'X'
        board.grid[2][3] = 'X'
        board.grid[1][4] = 'X'

        board.print_grid()

        self.assertTrue(board.look_for_4_positive_slopes())




if __name__=='__main__':
    unittest.main()


