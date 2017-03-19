import copy

from Node import Node

class ActionDown():

    name = 'down'

    def execute_action(self,node):
        if node.can_down():
            node_copy = copy.deepcopy(node)
            down_son = Node(node_copy.down(),node,self)
            return down_son

    def get_name(self):
       return self.name


