import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Node import Node as Nd

#############################
# LINKED LIST
#############################
class LinkedList(object):

    def __init__(self, head_node=None):
        self.head, self.size = head_node, 1


    # Insert Node at begining, taking O(1) to add node
    def insert_begin(self, data):
        new_node, new_node.next_node = Nd.Node(data), self.head
        self.head = new_node
        self.print_list()

    def insert_begin_byNode(self, Nd):
        new_node, new_node.next_node = Nd, self.head
        self.head = new_node
        self.print_list()


    # Insert Node based on a given position
    def insert_middle(self, data, before_data, after_data):
        curr_node, new_node = self.head, Nd.Node(data)

        # find the node with before data, worst case O(n)
        while(curr_node.next_node):
            nxt_2_curr_node = curr_node.next_node

            # next node with after data, insert in middle
            if curr_node.data == before_data and nxt_2_curr_node.data == after_data:
                curr_node.next_node, new_node.next_node = new_node, nxt_2_curr_node
                break
            else:
                curr_node = curr_node.next_node
        self.print_list()


    # Insert Node at end
    def insert(self, data):
        new_node = Nd.Node(data)

        if self.head is None:
            self.head = new_node
        else:
            # find the last node, step responsible for O(n)
            curr_node = self.head
            while (curr_node.next_node):
                curr_node = curr_node.next_node
            curr_node.next_node = new_node
        self.print_list()

    # Delete by Node
    def delete(self, data):
        prev_node = None
        curr_node = self.head

        found = False
        while (found is False):
            if (curr_node is None):
                print 'Node is not present'
                return
            elif curr_node.data == data:
                found = True
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node

        if prev_node is None:
            self.head = curr_node.next_node
        else:
            prev_node.next_node = curr_node.next_node
        self.print_list()

    def Delete_by_Node(self, Nd):
        prev_node = None
        curr_node = self.head

        found = False
        while (found is False):
            if (curr_node is None):
                print 'Node is not present'
                return
            elif curr_node == Nd:
                found = True
            else:
                prev_node = curr_node
                curr_node = curr_node.next_node

        if prev_node is None:
            self.head = curr_node.next_node
        else:
            prev_node.next_node = curr_node.next_node
        self.print_list()

    # Print Linked List, can be done with __str__ method also
    def print_list(self):
        curr_node, out_text = self.head, 'Head --> '
        while(curr_node):
            out_text += str(curr_node.data) + ' --> '
            curr_node = curr_node.next_node
        out_text += '*'
        print out_text


#############################
# USAGE
#############################
if __name__ == '__main__':
    lst = LinkedList()
    print '-- Insert --'
    lst.insert(10)                  # 10 --> *
    lst.insert(20)                  # 10 --> 20 --> *
    lst.insert(30)                  # 10 --> 20 --> 30 --> *
    lst.insert(500)                 # 10 --> 20 --> 30 --> 500 --> *
    lst.insert_middle(15, 10, 20)   # 10 --> 15 --> 20 --> 30 --> 500 --> *
    lst.insert_middle(25, 20, 30)   # 10 --> 15 --> 20 --> 25 --> 30 --> 500 --> *
    lst.insert_begin(2)             # 2 --> 10 --> 15 --> 20 --> 25 --> 30 --> 500 --> *
    lst.insert_begin(100)

    print '-- Delete --'
    lst.insert_begin(10)
    lst.delete(10)
    lst.delete(11111)
    # lst.print_list()

    print '-- Insert by Node --'
    n = Nd.Node(1)
    lst.insert_begin_byNode(n)
    lst.Delete_by_Node(n)
