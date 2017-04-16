import unittest

from InteligenciaArtificial.TP2ConnectFour.Players import Player
from InteligenciaArtificial.TP2ConnectFour.Board import Board

class PlayersTest(unittest.TestCase):


    #Vertical lines

    def test_find_0_vertical_c2s_when_there_are_not(self):

        board = Board()

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(0, player.find_how_many_n_vertical_availiable(2))

    def test_find_2_vertical_c2s(self):

        board = Board()
        board.grid[1][1] = 'O'
        board.grid[2][1] = 'O'
        board.grid[0][3] = 'O'
        board.grid[1][3] = 'O'

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(2, player.find_how_many_n_vertical_availiable(2))


    def test_find_1_vertical_c2s_when_there_is_only_1_aviliable_of_2(self):

        board = Board()
        board.grid[0][1] = 'O'
        board.grid[1][1] = 'X'
        board.grid[2][1] = 'X'
        board.grid[3][1] = 'O'
        board.grid[0][3] = 'X'
        board.grid[1][3] = 'X'

        player = Player('X', board)

        board.print_grid()

        self.assertEquals(1, player.find_how_many_n_vertical_availiable(2))


    def test_find_2_vertical_c3s_when_there_are_only_2_aviliable_of_4(self):

        board = Board()
        board.grid[0][1] = 'X'
        board.grid[1][1] = 'X'
        board.grid[2][1] = 'X'
        board.grid[3][2] = 'X'
        board.grid[4][2] = 'X'
        board.grid[5][2] = 'X'
        board.grid[2][6] = 'O'
        board.grid[3][6] = 'X'
        board.grid[4][6] = 'X'
        board.grid[5][6] = 'X'
        board.grid[0][5] = 'X'
        board.grid[1][5] = 'X'
        board.grid[2][5] = 'X'
        board.grid[3][5] = 'O'

        player = Player('X', board)

        board.print_grid()

        self.assertEquals(2, player.find_how_many_n_vertical_availiable(3))



    #Horizontal lines

    def test_find_0_horizontal_c2s_when_there_are_not(self):

        board = Board()

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(0, player.find_how_many_n_horizontal_availiable(2))


    def test_find_2_horizontal_c2s(self):

        board = Board()
        board.grid[0][1] = 'O'
        board.grid[0][2] = 'O'
        board.grid[1][3] = 'O'
        board.grid[1][4] = 'O'

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(2, player.find_how_many_n_horizontal_availiable(2))


    def test_find_1_horizontal_c3s_when_there_is_only_1_aviliable_of_2(self):

        board = Board()
        board.grid[0][1] = 'O'
        board.grid[0][2] = 'O'
        board.grid[0][3] = 'O'
        board.grid[3][3] = 'X'
        board.grid[3][4] = 'O'
        board.grid[3][5] = 'O'
        board.grid[3][6] = 'O'

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(1, player.find_how_many_n_horizontal_availiable(3))


    def test_find_2_horizontal_c3s_when_there_are_only_2_aviliable_of_4(self):

        board = Board()
        board.grid[0][0] = 'X'
        board.grid[0][1] = 'X'
        board.grid[0][2] = 'X'
        board.grid[0][3] = 'O'
        board.grid[1][0] = 'X'
        board.grid[1][1] = 'X'
        board.grid[1][2] = 'X'
        board.grid[3][4] = 'X'
        board.grid[3][5] = 'X'
        board.grid[3][6] = 'X'
        board.grid[5][1] = 'O'
        board.grid[5][2] = 'X'
        board.grid[5][3] = 'X'
        board.grid[5][4] = 'X'
        board.grid[5][5] = 'O'

        player = Player('X', board)

        board.print_grid()

        self.assertEquals(2, player.find_how_many_n_horizontal_availiable(3))


#Diagonal lines

    def test_find_0_negative_diagonal_c2s_when_there_are_not(self):

        board = Board()

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(0, player.find_how_many_n_negative_slopes_availiable(2))


    def test_find_2_negative_diagonal_c2s(self):

        board = Board()
        board.grid[0][1] = 'O'
        board.grid[1][2] = 'O'
        board.grid[3][3] = 'O'
        board.grid[4][4] = 'O'

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(2, player.find_how_many_n_negative_slopes_availiable(2))


    def test_find_1_negative_diagonal_c3s_when_there_is_only_1_aviliable_of_2(self):

        board = Board()
        board.grid[0][0] = 'O'
        board.grid[1][1] = 'O'
        board.grid[2][2] = 'O'
        board.grid[3][3] = 'X'
        board.grid[3][4] = 'O'
        board.grid[4][5] = 'O'
        board.grid[5][6] = 'O'

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(1, player.find_how_many_n_negative_slopes_availiable(3))

"""
    def test_find_0_positive_diagonal_c2s_when_there_are_not(self):

        board = Board()

        player = Player('O', board)

        board.print_grid()

        self.assertEquals(0, player.find_how_many_n_positive_slopes_availiable(2))
"""
if __name__=='__main__':
    unittest.main()