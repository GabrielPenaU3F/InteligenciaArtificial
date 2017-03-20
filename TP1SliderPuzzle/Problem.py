import copy

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
                        if (child not in explored) and (child is not None):
                            frontier.append(child)


            else: #If the frontier is empty and there are no more nodes to add...
                print 'This problem has no solution'


    def goal(self, node): #Check if a node contains the solution
        state = node.get_state()
        goal = True
        for i in range(len(state)-1):
            if state[i] > state[i+1]:
                goal = False

        return goal


    def solution(self, node): #Calculate the solution and show it step by step
        actions = 'Moves '
        solution_node = copy.deepcopy(node)
        number_of_moves = 0
        while (node.get_parent() is not None):
            actions = actions + (node.get_parent_action().get_name() + ' ')
            node = node.get_parent()
            number_of_moves += 1

        print actions
        print ('Total: %d  moves') %(number_of_moves)
        print 'From ' + str(self.zero_node.get_state())



    def convert_to_int(self, parameters):
        int_params = deque()
        for parameter in parameters:
            int_params.append(int(parameter))

        return int_params