import copy

import itertools

from Node import Node
from ActionDown import ActionDown
from ActionUp import ActionUp
from ActionRight import ActionRight
from ActionLeft import ActionLeft
from collections import deque

class Problem():

    zero_node = ()
    actions = deque()

    def __init__(self, parameters):
        int_params = self.convert_to_int(parameters)
        self.zero_node = Node(int_params, None, None)
        self.actions.append(ActionDown())
        self.actions.append(ActionUp())
        self.actions.append(ActionRight())
        self.actions.append(ActionLeft())
        self.graph_search_bfs()



    def graph_search_bfs(self):
        frontier = deque()
        explored = deque()
        frontier.append(self.zero_node);
        loop = True
        while loop:
            if frontier: #This gets true if the list is not empty
                node = frontier.popleft()
                if self.goal(node):
                    print self.solution(node)
                    loop = False

                else:
                    explored.append(node)
                    for action in self.actions:
                        node_copy = copy.deepcopy(node)
                        child = action.execute_action(node_copy)
                        if (child is not None):
                            if (child.is_not_in(explored) and child.is_not_in(frontier)):
                                frontier.append(child)


            else: #If the frontier is empty and there are no more nodes to add...
                print 'This problem has no solution'
                loop = False


    def goal(self, node): #Check if a node contains the solution
        state = node.get_state()
        goal = True
        for i in range(len(state)-1):
            if state[i] > state[i+1]:
                goal = False

        return goal


    def solution(self, node): #Calculate the solution and show it step by step
        actions = 'Moves '
        list_of_actions = list()
        list_of_states = list()
        number_of_moves = 0
        while (node.get_parent() is not None):
            list_of_actions.append(node.get_parent_action().get_name())
            list_of_states.append(node.get_state())
            node = node.get_parent()
            number_of_moves += 1

        list_of_actions.reverse()
        list_of_states.append(self.zero_node.get_state())
        list_of_states.reverse()
        for i in list_of_actions:
            actions = actions + (i + ' ')

        for i in list_of_states:
            self.print_state(i)

        print actions
        print ('Total: %d  moves') %(number_of_moves)
        print 'From ' + str(self.zero_node.get_state())



    def convert_to_int(self, parameters):
        int_params = deque()
        for parameter in parameters:
            int_params.append(int(parameter))

        return int_params

    def print_state(self, state):
        first_row = self.build_string(list(itertools.islice(state,0,3)))
        second_row = self.build_string(list(itertools.islice(state,3,6)))
        third_row = self.build_string(list(itertools.islice(state,6,9)))
        print ('\n%s\n%s\n%s\n') % (first_row, second_row, third_row)

    def build_string(self, structure):
        string = ''
        for i in structure:
            string += (str(i) + '')

        return string