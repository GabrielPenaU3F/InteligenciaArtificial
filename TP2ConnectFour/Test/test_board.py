import unittest

from InteligenciaArtificial.TP2ConnectFour.Board import Board
from InteligenciaArtificial.TP2ConnectFour.Game import Game
from InteligenciaArtificial.TP2ConnectFour.Players import *


class BoardTest(unittest.TestCase):

    def test_do_not_find_vertical_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_vertical('O'))


    def test_do_not_find_horizontal_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_horizontal('O'))


    def test_do_not_find_positive_diagonal_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_positive_slopes('O'))


    def test_do_not_find_negative_diagonal_c4(self):

        board = Board()

        self.assertFalse(board.look_for_4_negative_slopes('O'))


    def test_find_vertical_c4(self):

        board = Board()
        board.grid[1][2] = 'O'
        board.grid[2][2] = 'O'
        board.grid[3][2] = 'O'
        board.grid[4][2] = 'O'

        board.print_grid()

        self.assertTrue(board.look_for_4_vertical('O'))


    def test_find_horizontal_c4(self):

        board = Board()
        board.grid[3][3] = 'X'
        board.grid[3][4] = 'X'
        board.grid[3][5] = 'X'
        board.grid[3][6] = 'X'

        board.print_grid()

        self.assertTrue(board.look_for_4_horizontal('X'))


    def test_find_negative_diagonal_c4(self):

        board = Board()
        board.grid[1][1] = 'X'
        board.grid[2][2] = 'X'
        board.grid[3][3] = 'X'
        board.grid[4][4] = 'X'

        board.print_grid()

        self.assertTrue(board.look_for_4_negative_slopes('X'))


    def test_find_positive_diagonal_c4(self):

        board = Board()
        board.grid[4][1] = 'X'
        board.grid[3][2] = 'X'
        board.grid[2][3] = 'X'
        board.grid[1][4] = 'X'

        board.print_grid()

        self.assertTrue(board.look_for_4_positive_slopes('X'))

    def test_not_find_positive_diagonal_c4(self):
        board = Board()
        board.grid[1][1] = 'X'
        board.grid[2][1] = 'X'
        board.grid[0][3] = 'X'
        board.grid[1][3] = 'X'

        board.print_grid()

        self.assertFalse(board.look_for_4_positive_slopes('X'))


    def test_find_positive_diagonal_c4_when_it_is_at_the_bottom_right(self):

        board = Board()
        board.grid[2][6] = 'O'
        board.grid[3][5] = 'O'
        board.grid[4][4] = 'O'
        board.grid[5][3] = 'O'

        board.print_grid()

        self.assertTrue(board.look_for_4_diagonal('O'))


    def test_empty_column_is_not_full(self):

        board = Board()

        board.print_grid()

        self.assertTrue(board.column_not_full(3))


    def test_full_column_is_full(self):

        board = Board()

        for y in xrange(6):

            board.grid[y][3] = 'X'

        board.print_grid()

        self.assertFalse(board.column_not_full(3))


    def test_insert_into_empty_column(self):

        board = Board()

        board.insert_in_column(2, 'O')
        board.print_grid()

        self.assertEquals('O', board.grid[5][2])


    def test_insert_into_non_empty_column(self):

        board = Board()
        board.grid[5][2] = 'O'
        board.grid[4][2] = 'X'

        board.insert_in_column(2, 'O')
        board.print_grid()

        self.assertEquals('O', board.grid[3][2])


    #######


    # Vertical lines

    def test_find_0_vertical_c2s_when_there_are_not(self):
        board = Board()


        board.print_grid()

        self.assertEquals(0, board.find_how_many_n_vertical_availiable('O', 2))

    def test_find_2_vertical_c2s(self):
        board = Board()
        board.grid[1][1] = 'O'
        board.grid[2][1] = 'O'
        board.grid[0][3] = 'O'
        board.grid[1][3] = 'O'

        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_vertical_availiable('O', 2))

    def test_find_1_vertical_c2s_when_there_is_only_1_aviliable_of_2(self):
        board = Board()
        board.grid[0][1] = 'O'
        board.grid[1][1] = 'X'
        board.grid[2][1] = 'X'
        board.grid[3][1] = 'O'
        board.grid[0][3] = 'X'
        board.grid[1][3] = 'X'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_vertical_availiable('X', 2))

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

        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_vertical_availiable('X', 3))

    # Horizontal lines

    def test_find_0_horizontal_c2s_when_there_are_not(self):
        board = Board()

        board.print_grid()

        self.assertEquals(0, board.find_how_many_n_horizontal_availiable('O', 2))

    def test_find_2_horizontal_c2s(self):
        board = Board()
        board.grid[0][1] = 'O'
        board.grid[0][2] = 'O'
        board.grid[1][3] = 'O'
        board.grid[1][4] = 'O'

        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_horizontal_availiable('O', 2))

    def test_find_1_horizontal_c3s_when_there_is_only_1_aviliable_of_2(self):
        board = Board()
        board.grid[0][1] = 'O'
        board.grid[0][2] = 'O'
        board.grid[0][3] = 'O'
        board.grid[3][3] = 'X'
        board.grid[3][4] = 'O'
        board.grid[3][5] = 'O'
        board.grid[3][6] = 'O'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_horizontal_availiable('O', 3))

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

        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_horizontal_availiable('X', 3))


        # Diagonal lines

    def test_find_0_negative_diagonal_c2s_when_there_are_not(self):
        board = Board()

        board.print_grid()

        self.assertEquals(0, board.find_how_many_n_negative_slopes_availiable('O', 2))

    def test_find_2_negative_diagonal_c2s(self):
        board = Board()
        board.grid[0][1] = 'O'
        board.grid[1][2] = 'O'
        board.grid[3][3] = 'O'
        board.grid[4][4] = 'O'

        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_negative_slopes_availiable('O', 2))

    def test_find_1_negative_diagonal_c3s_when_there_is_only_1_aviliable_of_2(self):
        board = Board()
        board.grid[0][0] = 'O'
        board.grid[1][1] = 'O'
        board.grid[2][2] = 'O'
        board.grid[3][3] = 'X'
        board.grid[3][4] = 'O'
        board.grid[4][5] = 'O'
        board.grid[5][6] = 'O'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_negative_slopes_availiable('O', 3))

    def test_find_0_positive_diagonal_c2s_when_there_are_not(self):
        board = Board()

        board.print_grid()

        self.assertEquals(0, board.find_how_many_n_positive_slopes_availiable('O', 2))

    def test_find_2_positive_diagonal_c2s(self):
        board = Board()
        board.grid[0][3] = 'X'
        board.grid[1][2] = 'X'
        board.grid[5][3] = 'X'
        board.grid[4][4] = 'X'

        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_positive_slopes_availiable('X', 2))

    def test_find_2_positive_diagonal_c3s_when_there_are_only_2_aviliable_of_3(self):
        board = Board()
        board.grid[0][2] = 'O'
        board.grid[1][1] = 'O'
        board.grid[2][0] = 'O'
        board.grid[3][3] = 'O'
        board.grid[2][4] = 'O'
        board.grid[1][5] = 'O'
        board.grid[3][2] = 'O'
        board.grid[4][1] = 'O'
        board.grid[5][0] = 'O'


        board.print_grid()

        self.assertEquals(2, board.find_how_many_n_positive_slopes_availiable('O', 3))


    def test_find_1_horizontal_c2_when_there_is_1_c2s_and_1_c3(self):

        board = Board()

        board.grid[0][1] = 'X'
        board.grid[0][2] = 'X'
        board.grid[0][3] = 'X'
        board.grid[2][2] = 'X'
        board.grid[2][3] = 'X'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_horizontal_availiable('X', 2))

    def test_find_1_vertical_c2_when_there_is_1_c2s_and_1_c3(self):

        board = Board()

        board.grid[1][0] = 'X'
        board.grid[2][0] = 'X'
        board.grid[3][0] = 'X'
        board.grid[4][3] = 'X'
        board.grid[5][3] = 'X'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_vertical_availiable('X', 2))


    def test_find_1_negative_diagonal_c2_when_there_is_1_c2s_and_1_c3(self):

        board = Board()

        board.grid[1][1] = 'X'
        board.grid[2][2] = 'X'
        board.grid[3][3] = 'X'
        board.grid[1][3] = 'X'
        board.grid[2][4] = 'X'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_negative_slopes_availiable('X', 2))

    def test_find_1_positive_diagonal_c2_when_there_is_1_c2s_and_1_c3(self):

        board = Board()

        board.grid[4][1] = 'X'
        board.grid[3][2] = 'X'
        board.grid[2][3] = 'X'
        board.grid[3][4] = 'X'
        board.grid[2][5] = 'X'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_positive_slopes_availiable('X', 2))


    def test_find_1_X_c2_1_X_c3_1_O_c2_and_2_O_c2(self):

        board = Board()

        board.grid[5][0] = 'X'
        board.grid[5][1] = 'X'
        board.grid[5][3] = 'O'
        board.grid[5][4] = 'O'
        board.grid[5][5] = 'O'
        board.grid[4][3] = 'X'
        board.grid[4][4] = 'O'
        board.grid[4][5] = 'O'
        board.grid[3][4] = 'X'
        board.grid[3][5] = 'O'
        board.grid[2][5] = 'X'

        board.print_grid()

        self.assertEquals(1, board.find_how_many_n_horizontal_availiable('X', 2))
        self.assertEquals(1, board.find_how_many_n_horizontal_availiable('O', 2))
        self.assertEquals(1, board.find_how_many_n_positive_slopes_availiable('X', 3))
        self.assertEquals(1, board.find_how_many_n_positive_slopes_availiable('O', 3))

        self.assertEquals(0, board.find_how_many_n_negative_slopes_availiable('X', 3))
        self.assertEquals(0, board.find_how_many_n_negative_slopes_availiable('O', 3))
        self.assertEquals(0, board.find_how_many_n_vertical_availiable('X', 3))
        self.assertEquals(0, board.find_how_many_n_vertical_availiable('O', 3))


    def test_tree_generation(self):

        board = Board()

        for y in xrange(6):
            for x in xrange(7):

                board.grid[y][x] = 'O'

        board.grid[0][0] = '-'
        board.grid[1][0] = '-'
        board.grid[0][1] = '-'
        board.grid[1][1] = '-'

        game = Game()
        game.set_board(board)
        player1 = HumanPlayer('X', game)
        player2 = IAPlayer('O', game)
        game.players.append(player1)
        game.players.append(player2)

        p2_board = player2.assigned_board
        gen = game.tree_gen
        new_board = gen.generate_tree(p2_board, 3, 'X', True)

        print '\n Minimax Tree \n'

        level_1_nodes = []
        level_2_nodes = []
        level_3_nodes = []

        for x in xrange(new_board.children.__len__()):
            child = new_board.children[x]
            level_1_nodes.append(child)

        for x in xrange(level_1_nodes.__len__()):
            for y in xrange(level_1_nodes[x].children.__len__()):

                child = level_1_nodes[x].children[y]
                level_2_nodes.append(child)

        for x in xrange(level_2_nodes.__len__()):
            for y in xrange(level_2_nodes[x].children.__len__()):

                child = level_2_nodes[x].children[y]
                level_3_nodes.append(child)

        #Print every node by level

        print 'Level 1 Nodes \n'

        for x in xrange(level_1_nodes.__len__()):
            level_1_nodes[x].print_grid()
            print '\n'

        print 'Level 2 Nodes \n'

        for x in xrange(level_2_nodes.__len__()):
            level_2_nodes[x].print_grid()
            print '\n'

        print 'Level 3 Nodes \n'

        for x in xrange(level_3_nodes.__len__()):
            level_3_nodes[x].print_grid()
            print '\n'
            


if __name__=='__main__':
    unittest.main()