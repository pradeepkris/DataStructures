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

class LinkedList(object):

    def __init__(self, head_node=None):
        self.head = head_node
        self.size = 1

    # Insert Node at begining, taking O(1) to add node
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # Insert Node at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            # find the last node, step responsible for O(n)
            curr_node = self.head
            while (curr_node.next_node):
                curr_node = curr_node.next_node
            curr_node.next_node = new_node


    def print_list(self):
        curr_node, out_text = self.head, ''
        while(curr_node):
            out_text += str(curr_node.data) + ' --> '
            curr_node = curr_node.next_node

        out_text += '*'
        print out_text


lst = LinkedList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.insert(5)
lst.insert_begin(2)
lst.print_list()
