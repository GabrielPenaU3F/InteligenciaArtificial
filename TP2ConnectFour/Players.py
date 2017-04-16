class Player():

    def __init__(self, player_string, board):

        self.assigned_board = board
        self.player_string = player_string #Here goes 'X' or 'O'
        self.grid = self.assigned_board.get_grid()

    def won(self):

        pass #TODO: implement


    def count_lined_possibilities_by_number(self, number):  # Count how many line-2 or line-3 the player has
        lines = 0
        lines += self.find_how_many_n_vertical_availiable(number)
        lines += self.find_how_many_n_horizontal_availiable(number)
        lines += self.find_how_many_n_diagonal_availiable(number)
        return lines


    def find_how_many_n_vertical_availiable(self, n):

            total_count = 0
            count = 0
            for x in xrange(7):  # Width
                for y in xrange(7 - n):
                    for i in xrange(1, n):
                        if (self.grid[y][x] == self.grid[y + i][x] and self.grid[y][x] == self.player_string):
                            count += 1

                        else:
                            count = 0
                            break

                    # Availiability check
                    if (y == 0):

                        if (self.grid[y + n][x] == '-'):

                            if count == n-1:  #n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                    elif (y > 0 and y < 6 - n):

                        if (self.grid[y - 1][x] == '-' or self.grid[y + n][x] == '-'):

                            if count == n-1:  #n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                    elif (y == 6-n):

                        if (self.grid[y - 1][x] == '-'):

                            if count == n-1:  #n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0


            return total_count

    def find_how_many_n_horizontal_availiable(self, n):

            total_count = 0
            count = 0
            for y in xrange(6):  # Height
                for x in xrange(8-n):
                    for i in xrange(1, n):
                        if (self.grid[y][x] == self.grid[y][x + i] and self.grid[y][x] == self.player_string):
                            count += 1

                        else:
                            count = 0
                            break

                    # Availiability check
                    if (x == 0):

                        if (self.grid[y][x + n] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                    elif (x > 0 and x < 7 - n):

                        if (self.grid[y][x - 1] == '-' or self.grid[y][x + n] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                    elif (x == 7 - n):

                        if (self.grid[y][x - 1] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

            return total_count


    def find_how_many_n_diagonal_availiable(self, n):

            positive_slopes = self.find_how_many_n_positive_slopes_availiable()
            negative_slopes = self.find_how_many_n_negative_slopes_availiable()

            return positive_slopes + negative_slopes

    def find_how_many_n_negative_slopes_availiable(self, n):

            total_count = 0
            count = 0
            for x in xrange(8-n):
                for y in xrange(7-n):
                    for i in xrange(1, n):
                        if self.grid[y][x] == self.grid[y + i][x + i] and self.grid[y][x] == self.player_string:
                            count += 1
                        else:
                            count = 0
                            break

                    # Availiability check

                    if (y == 0):

                        if (x >= 0 and x < 7 - n):

                            if (self.grid[y + n][x + n] == '-'):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0

                        else: count = 0

                    elif (y > 0 and y < 6 - n):

                        if (x == 0):  # TODO: especificar que ocurre en cada esquina


                            if (self.grid[y + n][x + n] == '-'):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0

                        elif (x > 0 and x < 7 - n):

                            if (self.grid[y - 1][x - 1] == '-' or self.grid[y + n][x + n] == '-'):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0


                        elif (x == 7 - n):

                            if (self.grid[y - 1][x - 1] == '-'):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0


                    elif (y == 6 - n):

                        if (x > 0 and x <= 7 - n):

                            if (self.grid[y - 1][x - 1] == '-'):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0

                        else: count = 0

            return total_count

    def find_how_many_n_positive_slopes_availiable(self, n):

        total_count = 0
        count = 0
        for y in xrange(7 - n):
            for x in xrange(n - 1, 7):
                for i in xrange(1, n):
                    if self.grid[y][x] == self.grid[y + i][x - i] and self.grid[y][x] == self.player_string:
                        count += 1
                    else:
                        count = 0
                        break

                # Availiability check

                if (y == 0):

                    if (x >= n):

                        if (self.grid[y + n][x - n] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                    else:
                        count = 0

                elif (y > 0 and y < 5 - (n - 1)):

                    if (x >= n and x < 6):


                        if (self.grid[y + n][x - n] == '-' or self.grid[y - 1][x + 1] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                    elif (x == 6):

                        if (self.grid[y + n][x - n] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                elif (y == 5 - (n - 1)):

                    if (x < 6):

                        if (self.grid[y - 1][x + 1] == '-'):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0




        return total_count


###############################

class HumanPlayer(Player):


    def move(self):

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


    def put(self, column_index):

        self.board.insert_in_column(column_index, self.player_string)


class IAPlayer(Player):

    pass