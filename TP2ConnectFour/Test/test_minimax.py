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


    #Manual test. Allows watching the Minimax tree
    def test_minimax(self):

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

        game = Game()
        game.set_board(board)
        player1 = HumanPlayer('X', game)
        player2 = IAPlayer('O', game)
        game.players.append(player1)
        game.players.append(player2)

        p2_board = player2.assigned_board
        gen = game.tree_gen
        new_board = gen.generate_tree(p2_board, 3, 'O', True)
        player2.build_minimax(new_board)

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
            level_1_nodes[x].print_value()
            print '\n'

        print 'Level 2 Nodes \n'

        for x in xrange(level_2_nodes.__len__()):
            level_2_nodes[x].print_grid()
            level_2_nodes[x].print_value()
            print '\n'

        print 'Level 3 Nodes \n'

        for x in xrange(level_3_nodes.__len__()):
            level_3_nodes[x].print_grid()
            level_3_nodes[x].print_value()
            print '\n'

    if __name__ == '__main__':
        unittest.main()