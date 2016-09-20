#############################
# NODE
#############################
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

#############################
# LINKED LIST
#############################
class LinkedList(object):

    def __init__(self, head_node=None):
        self.head, self.size = head_node, 1


    # Insert Node at begining, taking O(1) to add node
    def insert_begin(self, data):
        new_node, new_node.next_node = Node(data), self.head
        self.head = new_node


    # Insert Node based on a given position
    def insert_middle(self, data, before_data, after_data):
        curr_node, new_node = self.head, Node(data)

        # find the node with before data, worst case O(n)
        while(curr_node.next_node):
            nxt_2_curr_node = curr_node.next_node

            # next node with after data, insert in middle
            if curr_node.data == before_data and nxt_2_curr_node.data == after_data:
                curr_node.next_node, new_node.next_node = new_node, nxt_2_curr_node
                break
            else:
                curr_node = curr_node.next_node


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

    # Delete by Node
    def delete_by_Node(self, Node):
        prev_node = None
        curr_node = self.head

        found = False
        while (found is True):
            if curr_node == Node:
                found = True
            elif (curr_node is None):
                print 'Node is not present'
                break
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node

        if prev_node is None:
            self.head = curr_node.next_node
        else:
            prev_node.next_node = curr_node.next_node


    # Print Linked List, can be done with __str__ method also
    def print_list(self):
        curr_node, out_text = self.head, ''
        while(curr_node):
            out_text += str(curr_node.data) + ' --> '
            curr_node = curr_node.next_node
        out_text += '*'
        print out_text


#############################
# USAGE
#############################
lst = LinkedList()
lst.insert(10)                  # 10 --> *
lst.insert(20)                  # 10 --> 20 --> *
lst.insert(30)                  # 10 --> 20 --> 30 --> *
lst.insert(500)                 # 10 --> 20 --> 30 --> 500 --> *
lst.insert_middle(15, 10, 20)   # 10 --> 15 --> 20 --> 30 --> 500 --> *
lst.insert_middle(25, 20, 30)   # 10 --> 15 --> 20 --> 25 --> 30 --> 500 --> *
lst.insert_begin(2)             # 2 --> 10 --> 15 --> 20 --> 25 --> 30 --> 500 --> *
lst.print_list()

n = Node(-7)
