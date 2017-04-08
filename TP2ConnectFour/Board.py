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


    def has_a_line_of_four(self):

        vertical_four = self.look_for_4_vertical()
        horizontal_four = self.look_for_4_horizontal()
        diagonal_four = self.look_for_4_diagonal()

        if (vertical_four==True or horizontal_four==True or diagonal_four==True):
            return True

        else: return False



    def look_for_4_vertical(self):

        count = 0
        for y in xrange(7): #Width
            for x in xrange(5): #Height-1
                if (self.grid[y][x] == self.grid[y][x+1]):
                    count+=1
                else: break

            if count==4: #ConnectFour!
                return True

        return False

    def look_for_4_horizontal(self):

        count = 0
        for x in xrange(6): #Height
            for y in xrange(6): #Width-1
                if (self.grid[y][x] == self.grid[y+1][x]):
                    count+=1
                else: break

            if count==4: #ConnectFour!
                return True

        return False

    def look_for_4_diagonal(self):

        positive_slopes = self.look_for_4_positive_slopes()
        negative_slopes = self.look_for_4_negative_slopes()

        if (positive_slopes==True or negative_slopes==True): return True
        else: return False


    def look_for_4_positive_slopes(self):

        count = 0
        for x in xrange(3): #Height-3
            for y in xrange(4): #Width-3
                for i in xrange(3):
                    if self.grid[0][0] == self.grid[y + i][x + i]:
                        count += 1
                    else:
                        break

    def look_for_4_negative_slopes(self):

        count = 0
        for x in xrange(3):  # Height-3
            for y in xrange(4):  # Width-3
                for i in xrange(3):
                    if self.grid[7][6] == self.grid[7 - y + i][6 - x + i]:
                        count += 1
                    else:
                        break