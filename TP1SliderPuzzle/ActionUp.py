import copy

from Node import Node

class ActionUp():

    name = 'up'

    def execute_action(self, node):
       if node.can_up():
           node_copy = copy.deepcopy(node)
           up_son = Node(node_copy.up(), node, self)
           return up_son

    def get_name(self):
       return self.name


