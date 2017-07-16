#############################
# NODE
#############################
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


#############################
# NODE with double link
#############################
class DNode(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
