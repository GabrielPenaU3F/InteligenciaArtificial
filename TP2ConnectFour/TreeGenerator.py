from copy import deepcopy

from Board import Board


class TreeGenerator():


    #Doesn't work
    def generate_tree(self, board, depth, player_string, player_flag):

        #The flag indicates if the tree has to be generated with
        #the proper player string (True) or with a symbol that represents
        #the other player (False)

        if (depth > 0):

            if (player_flag == True):

                self.generate_children(board, player_string)

            else: self.generate_children(board, '$')
            #The symbol $ represents 'the non-IA player'

            new_player_flag = not player_flag #Next turn, the next player plays


            for x in xrange(board.children.__len__()):

                self.generate_tree(board.children[x], depth - 1, player_string, new_player_flag)


        else: pass

        return board








    def generate_children(self, board, player_string):

        for x in xrange(7):

            if (board.column_not_full(x)):

                child = Board()
                child.set_grid(deepcopy(board.grid))
                child.set_player_string(player_string)
                child.set_father(board)
                child.insert_in_column(x, player_string)

                board.children.append(child)

    def destroy(self, board):

        board.children = []