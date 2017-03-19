class Node():

    state = ()
    parent = ()
    parent_action = ()
    total_cost = ()

    def __init__(self, state, parent, parent_action):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.total_cost = self.calculate_cost()

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_parent_action(self):
        return self.parent_action

    def get_cost(self):
        return self.cost

    def calculate_cost(self):
        if self.parent is None:
            return 0
        else:
            return self.parent.calculate_cost() + 1

    #Returns the position numbered 0..8 where the blank square is located
    def calculate_zero_position(self):
        for i in range(0,9):
            if self.state[i] == 0:
                return i

    #This decides wether or not you can move the blank square down in this state
    def can_down(self):
        positions_that_forbid_down = [6,7,8]
        if positions_that_forbid_down.__contains__(self.calculate_zero_position()):
            return False
        else:
            return True

    #This decides wether or not you can move the blank square up in this state
    def can_up(self):
        positions_that_forbid_up = [0,1,2]
        if positions_that_forbid_up.__contains__(self.calculate_zero_position()):
            return False
        else:
            return True

    #This decides wether or not you can move the blank square right in this state
    def can_right(self):
        positions_that_forbid_right = [2,5,8]
        if positions_that_forbid_right.__contains__(self.calculate_zero_position()):
            return False
        else:
            return True

    #This decides wether or not you can move the blank square left in this state
    def can_left(self):
        positions_that_forbid_left = [0,3,6]
        if positions_that_forbid_left.__contains__(self.calculate_zero_position()):
            return False
        else:
            return True

    def down(self):
            new_state = self.state
            zero_position = self.calculate_zero_position()
            aux = self.state[zero_position + 3]
            new_state[zero_position] = aux
            new_state[zero_position + 3] = 0
            return new_state

    def up(self):
            new_state = self.state
            zero_position = self.calculate_zero_position()
            aux = self.state[zero_position - 3]
            new_state[zero_position] = aux
            new_state[zero_position - 3] = 0
            return new_state

    def right(self):
            new_state = self.state
            zero_position = self.calculate_zero_position()
            aux = self.state[zero_position + 1]
            new_state[zero_position] = aux
            new_state[zero_position + 1] = 0
            return new_state

    def left(self):
            new_state = self.state
            zero_position = self.calculate_zero_position()
            aux = self.state[zero_position - 1]
            new_state[zero_position] = aux
            new_state[zero_position - 1] = 0
            return new_state
