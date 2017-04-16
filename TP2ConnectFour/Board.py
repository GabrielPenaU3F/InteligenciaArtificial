class Board():

    def __init__(self):


        #Define the dimensions and fill the blanks with -
        self.width = 7
        self.height = 6
        self.grid = []
        for y in xrange(self.height):
            self.grid.append([])
            for x in xrange(self.width):
                self.grid[y].append('-')


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


    def has_a_line_of_four(self):

        vertical_four = self.look_for_4_vertical()
        horizontal_four = self.look_for_4_horizontal()
        diagonal_four = self.look_for_4_diagonal()

        if (vertical_four==True or horizontal_four==True or diagonal_four==True):
            return True

        else: return False



    def look_for_4_vertical(self):

        count = 0
        for x in xrange(7): #Width
            for y in xrange(3):
                for i in xrange(1,4):
                    if (self.grid[y][x] == self.grid[y+i][x] and self.grid[y][x] != '-'):
                        count += 1

                    else:
                        count = 0
                        break

                if count==3: #ConnectFour!
                    return True

                else: count = 0

        return False

    def look_for_4_horizontal(self):

        count = 0
        for y in xrange(6):  #Height
            for x in xrange(4):
                for i in xrange(1, 4):
                    if (self.grid[y][x] == self.grid[y][x+i] and self.grid[y][x] != '-'):
                        count += 1

                    else:
                        count = 0
                        break

                if count == 3:  # ConnectFour!
                    return True

                else: count = 0

        return False

    def look_for_4_diagonal(self):

        positive_slopes = self.look_for_4_positive_slopes()
        negative_slopes = self.look_for_4_negative_slopes()

        if (positive_slopes==True or negative_slopes==True): return True
        else: return False


    def look_for_4_negative_slopes(self):

        count = 0
        for x in xrange(4): #Width-3
            for y in xrange(3): #Height-3
                for i in xrange(1,4):
                    if self.grid[y][x] == self.grid[y + i][x + i] and self.grid[y][x] != '-':
                        count += 1
                    else:
                        count=0
                        break

                if count == 3:
                    return True

                else: count = 0

        return False


    def look_for_4_positive_slopes(self):

        count = 0
        for y in xrange(3):  # Height-3
            for x in xrange(3, 7):  # Width-3
                for i in xrange(1,4):
                    if self.grid[y][x] == self.grid[y + i][x - i] and self.grid[y][x] != '-':
                        count += 1
                    else:
                        count = 0
                        break

                if count == 3:
                    return True

                else: count = 0

        return False