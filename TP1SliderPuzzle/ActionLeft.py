import copy

from Node import Node

class ActionLeft():

    name = 'left'

    def execute_action(self, node):
       if node.can_left():
           node_copy = copy.deepcopy(node)
           left_son = Node(node_copy.left(), node, self)
           return left_son

    def get_name(self):
       return self.name



