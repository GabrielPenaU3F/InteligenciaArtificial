class Board():

    def __init__(self):


        #Define the dimensions and fill the blanks with -
        self.father = None
        self.children = []
        self.width = 7
        self.height = 6
        self.grid = []
        for y in xrange(self.height):
            self.grid.append([])
            for x in xrange(self.width):
                self.grid[y].append('-')


    def generate_tree(self, depth, player_string, player_flag):

        #The flag indicates if the tree has to be generated with
        #the proper player string (True) or with a symbol that represents
        #the other player (False)

        if (depth > 0):

            if (player_flag == True):

                self.generate_children(player_string)

            else: self.generate_children('$')
            #The symbol $ represents 'the non-IA player'

            new_player_flag = not player_flag #Next turn, the next player plays


            for x in xrange(self.children.__len__()):

                self.children[x].generate_tree(depth - 1, player_string, new_player_flag)



    def generate_children(self, player_string):

        for x in xrange(7):

            if (self.column_not_full(x)):
                child = Board()
                child.set_grid(self.grid)
                child.set_player_string(player_string)
                child.set_father(self)
                child.insert_in_column(x, player_string)
                self.children.append(child)


    def assign_value(self, value):

        self.value = value


    def evaluate_value(self, player_string):

        points = 0

        #Adds points for lines of 'my symbol'
        #Subbstracts points for lines of '$'
        #Heuristic is the following
            #2-lines availiable to play another coin are worth 100
            #3-lines availiable to play another coin are worth 1000

        #Problem with this definition: does NOT consider cases like
        # X X - X  or other 'non-linear' cases

        points += 100 * (self.count_lined_possibilities_by_number(player_string, 2))
        points += 1000 * (self.count_lined_possibilities_by_number(player_string, 3))
        points -= 100 * (self.count_lined_possibilities_by_number('$', 2))
        points -= 1000 * (self.count_lined_possibilities_by_number('$', 3))

        return points


    def set_grid(self, grid):

        self.grid = grid


    def set_player_string(self, player_string):

        self.player_string = player_string

    def set_father(self, father):

        self.father = father

    def insert_in_column(self, column_index, symbol):

        counter = 0
        for y in xrange(6):

            if (self.grid[y][column_index] != '-'):

                self.grid[y-1][column_index] = symbol  #Put it above the first filled slot
                break

            counter += 1

        if (counter == 6):

            self.grid[5][column_index] = symbol #Put it at the bottom line


    def column_not_full(self, column_index):

        if (self.grid[0][column_index] != '-'): return False
        else: return True


    def get_grid(self):

        return self.grid


    def print_grid(self):

        grid_string = str()
        for y in xrange(6):
            for x in xrange(7):
                grid_string += (self.grid[y][x])

            grid_string += "\n"

        print grid_string


    def change_board_enemy_string(self, enemy_string):

        for x in xrange(7):
            for y in xrange(6):

                if (self.grid[y][x] == enemy_string):
                    self.grid[y][x] = '$'

    def restore_board_enemy_string(self, enemy_string):

        for x in xrange(7):
            for y in xrange(6):

                if (self.grid[y][x] == '$'):
                    self.grid[y][x] = enemy_string



    #########


    def has_a_line_of_four(self, player_string):

        vertical_four = self.look_for_4_vertical(player_string)
        horizontal_four = self.look_for_4_horizontal(player_string)
        diagonal_four = self.look_for_4_diagonal(player_string)

        if (vertical_four==True or horizontal_four==True or diagonal_four==True):
            return True

        else: return False



    def look_for_4_vertical(self, player_string):

        count = 0
        for x in xrange(7): #Width
            for y in xrange(3):
                for i in xrange(1,4):
                    if (self.grid[y][x] == self.grid[y+i][x] and self.grid[y][x] == player_string):
                        count += 1

                    else:
                        count = 0
                        break

                if count==3: #ConnectFour!
                    return True

                else: count = 0

        return False

    def look_for_4_horizontal(self, player_string):

        count = 0
        for y in xrange(6):  #Height
            for x in xrange(4):
                for i in xrange(1, 4):
                    if (self.grid[y][x] == self.grid[y][x+i] and self.grid[y][x] == player_string):
                        count += 1

                    else:
                        count = 0
                        break

                if count == 3:  # ConnectFour!
                    return True

                else: count = 0

        return False

    def look_for_4_diagonal(self, player_string):

        positive_slopes = self.look_for_4_positive_slopes(player_string)
        negative_slopes = self.look_for_4_negative_slopes(player_string)

        if (positive_slopes==True or negative_slopes==True): return True
        else: return False


    def look_for_4_negative_slopes(self, player_string):

        count = 0
        for x in xrange(4): #Width-3
            for y in xrange(3): #Height-3
                for i in xrange(1,4):
                    if self.grid[y][x] == self.grid[y + i][x + i] and self.grid[y][x] == player_string:
                        count += 1
                    else:
                        count=0
                        break

                if count == 3:
                    return True

                else: count = 0

        return False


    def look_for_4_positive_slopes(self, player_string):

        count = 0
        for y in xrange(3):  # Height-3
            for x in xrange(3, 7):  # Width-3
                for i in xrange(1,4):
                    if self.grid[y][x] == self.grid[y + i][x - i] and self.grid[y][x] == player_string:
                        count += 1
                    else:
                        count = 0
                        break

                if count == 3:
                    return True

                else: count = 0

        return False

    #
    #
    #
    #Look for 2 and 3 lines

    def count_lined_possibilities_by_number(self, player_string, number):  # Count how many line-2 or line-3 the player has
        lines = 0
        lines += self.find_how_many_n_vertical_availiable(player_string, number)
        lines += self.find_how_many_n_horizontal_availiable(player_string, number)
        lines += self.find_how_many_n_diagonal_availiable(player_string, number)
        return lines


    def find_how_many_n_vertical_availiable(self, player_string, n):

            total_count = 0
            count = 0
            for x in xrange(7):  # Width
                for y in xrange(7 - n):
                    for i in xrange(1, n):
                        if (self.grid[y][x] == self.grid[y + i][x] and self.grid[y][x] == player_string):
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

                        if (self.grid[y - 1][x] == '-' and self.grid[y + n][x] != player_string):

                            if count == n-1:  #n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                        elif (self.grid[y + n][x] == '-' and self.grid[y - 1][x] != player_string):

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

    def find_how_many_n_horizontal_availiable(self, player_string, n):

            total_count = 0
            count = 0
            for y in xrange(6):  # Height
                for x in xrange(8-n):
                    for i in xrange(1, n):
                        if (self.grid[y][x] == self.grid[y][x + i] and self.grid[y][x] == player_string):
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

                        if (self.grid[y][x - 1] == '-' and self.grid[y][x + n] != player_string):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                        elif (self.grid[y][x + n] == '-' and self.grid[y][x - 1] != player_string):

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


    def find_how_many_n_diagonal_availiable(self, player_string, n):

            positive_slopes = self.find_how_many_n_positive_slopes_availiable(player_string, n)
            negative_slopes = self.find_how_many_n_negative_slopes_availiable(player_string, n)

            return positive_slopes + negative_slopes

    def find_how_many_n_negative_slopes_availiable(self, player_string, n):

            total_count = 0
            count = 0
            for x in xrange(8-n):
                for y in xrange(7-n):
                    for i in xrange(1, n):
                        if self.grid[y][x] == self.grid[y + i][x + i] and self.grid[y][x] == player_string:
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

                        if (x == 0):


                            if (self.grid[y + n][x + n] == '-'):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0

                        elif (x > 0 and x < 7 - n):

                            if (self.grid[y - 1][x - 1] == '-' and self.grid[y + n][x + n] != player_string):

                                if count == n - 1:  # n-line found!
                                    total_count += 1
                                    count = 0

                                else:
                                    count = 0

                            elif (self.grid[y + n][x + n] == '-' and self.grid[y - 1][x - 1] != player_string):

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

    def find_how_many_n_positive_slopes_availiable(self, player_string, n):

        total_count = 0
        count = 0
        for y in xrange(7 - n):
            for x in xrange(n - 1, 7):
                for i in xrange(1, n):
                    if self.grid[y][x] == self.grid[y + i][x - i] and self.grid[y][x] == player_string:
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


                        if (self.grid[y + n][x - n] == '-' and self.grid[y - 1][x + 1] != player_string):

                            if count == n - 1:  # n-line found!
                                total_count += 1
                                count = 0

                            else:
                                count = 0

                        elif (self.grid[y - 1][x + 1] == '-' and self.grid[y + n][x - n] != player_string):

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