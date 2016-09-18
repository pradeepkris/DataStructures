class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next_node = n2
n2.next_node = n3



class LinkedList(object):

    def __init__(self, head_node=None):
        self.head = head_node
        self.size = 1

    # Insert Node at begining
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Delete Node at begining

    # Insert Node at end

    # Delete Node at end

    # Insert Node at Middle

    # Delete Node at Middle
