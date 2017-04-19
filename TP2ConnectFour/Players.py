class Player():

    def __init__(self, player_string, game):


        self.game = game
        self.assigned_board = game.get_board()
        self.assigned_board.set_player_string(player_string)
        self.player_string = player_string #Here goes 'X' or 'O'
        self.grid = self.assigned_board.get_grid()

    def won(self):

        if(self.board.has_a_line_of_four(self.player_string)): return True

        else: return False


    def put(self, column_index):

        self.board.insert_in_column(column_index, self.player_string)

    def obtain_enemy_string(self):

        if (self.player_string == 'O'): return 'X'
        else: return 'O'




###############################

class HumanPlayer(Player):


    def move(self):

        self.board = self.game.get_board()

        print self.board.get_grid()

        entry_column = raw_input('Choose a column from 1 to 7\n')

        if (entry_column == 1 or entry_column == 2 or entry_column == 3 or entry_column == 4 or entry_column == 5 or entry_column == 6 or entry_column == 7):

            column_index = entry_column - 1

            if (self.board.column_not_full(column_index)):

                self.put(column_index)

            else:

                print 'The column is full. Please play elsewhere'
                self.move()

        else:

            print 'Wrong entry. Please enter the column again'
            self.move()

        self.game.update_board(self.board)








class IAPlayer(Player):

    def move(self):

        self.board = self.game.get_board()

        depth = 3 #How many moves forward it looks

        enemy_string = self.obtain_enemy_string()

        self.board.change_board_enemy_string(enemy_string) #Replaces the other player symbol by '$' in the board

        self.board.generate_tree(depth, self.player_string, True)

        self.build_minimax(self.assigned_board)


        #TODO: Complete

        self.board.restore_board_enemy_string(enemy_string) #Restores the original board

        self.game.update_board(self.board)



    def build_minimax(self, board):

        if (board.children != []):

            for child in xrange(self.assigned_board.children):

                value = self.build_minimax(child)
                board.assign_value(value)

        else:

            value = board.evaluate_value(self.player_string)
            board.assign_value(value)




