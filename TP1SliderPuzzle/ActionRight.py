import copy

from Node import Node

class ActionRight():

    name = 'right'

    def execute_action(self, node):
       if node.can_right():
           node_copy = copy.deepcopy(node)
           right_son = Node(node_copy.right(), node, self)
           return right_son

    def get_name(self):
       return self.name



