from copy import deepcopy


class Player():

    def __init__(self, player_string, game):


        self.game = game
        self.assigned_board = game.get_board()
        self.assigned_board.set_player_string(player_string)
        self.player_string = player_string #Here goes 'X' or 'O'
        self.grid = self.assigned_board.get_grid()

    def won(self):

        if(self.assigned_board.has_a_line_of_four(self.player_string)):

            self.assigned_board.print_grid()
            print 'Player %s won!!' %(self.player_string)
            return True

        else: return False


    def put(self, column_index):

        self.assigned_board.insert_in_column(column_index, self.player_string)

    def obtain_enemy_string(self):

        if (self.player_string == 'O'): return 'X'
        else: return 'O'




###############################

class HumanPlayer(Player):


    def move(self):

        self.assigned_board = self.game.get_board()

        entry_column = raw_input('Choose a column from 1 to 7\n')

        if (entry_column == '1' or entry_column == '2' or entry_column == '3' or entry_column == '4' or entry_column == '5' or entry_column == '6' or entry_column == '7'):

            entry_column_int = int(entry_column)

            column_index = entry_column_int - 1

            if (self.assigned_board.column_not_full(column_index)):

                self.put(column_index)

            else:

                print 'The column is full. Please play elsewhere'
                self.move()

        else:

            print 'Wrong entry. Please enter the column again'
            self.move()

        self.game.update_board(self.assigned_board)

        self.assigned_board.print_grid()








class IAPlayer(Player):

    def move(self):

        depth = 3 #How many moves forward it looks

        enemy_string = self.obtain_enemy_string()

        self.assigned_board.change_board_enemy_string(enemy_string) #Replaces the other player symbol by '$' in the board

        final_board = self.game.tree_gen.generate_tree(self.assigned_board, depth, self.player_string, True)

        self.build_minimax(final_board)

        self.assigned_board = final_board

        target = self.assigned_board.find_child_with_max_value()

        self.assigned_board.grid = deepcopy(target.grid)

        self.assigned_board.restore_board_enemy_string(enemy_string) #Restores the original board

        self.game.update_board(self.assigned_board)

        self.destroy_tree()

        self.assigned_board.print_grid()



    def build_minimax(self, board):

        if (board.children != []):

            for x in xrange(board.children.__len__()):

                child = board.children[x]
                self.build_minimax(child)
                value = board.calculate_value_from_children()
                board.assign_value(value)

        else:

            value = board.evaluate_value(self.player_string)
            board.assign_value(value)



    def destroy_tree(self):

        self.game.tree_gen.destroy(self.assigned_board)





