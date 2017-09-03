import sys, os
ROOT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_FOLDER)
from Node import Node as Nd

#############################
# LINKED LIST
#############################
class LinkedList(object):

    # Initialize linked list with given data #
    def __init__(self, data):
        self.head, self.size = Nd.Node(data), 1

    # Str dundr method #
    def __str__(self):
        curr_node, out_text = self.head, 'Head --> '
        while(curr_node):
            out_text += str(curr_node.data) + ' --> '
            curr_node = curr_node.next_node
        out_text += '*'
        return out_text

    # Insert by position #
    def insert(self, data, pos=0):
        # At begining, taking O(1) to add node
        new_node = Nd.Node(data)
        if pos == 0:
            head_node = self.head
            self.head = new_node
            new_node.next_node = head_node

        # At middle & end, taking O(n)for searching and O(1) for inserting
        elif pos > 0:
            # Find the position
            tempPointer = self.head
            for x in range(0, pos-1):
                if tempPointer.next_node is None: break
                tempPointer = tempPointer.next_node

            new_node.next_node = tempPointer.next_node
            tempPointer.next_node = new_node

        self.size += 1

    # Insert at the end of list #
    def append(self, data):
        self.insert(data, self.size + 1)

    # Delete by data or node #
    # This function deletes only the first occurance #
    # Todo: Unsorted: Scan entire list to delete all nodes with given data
    # Todo: Sorted: Use binary search to find the node(s) and delete
    def delete(self, del_item):
        prev_node = None
        curr_node = self.head

        found = False
        while (found is False):
            if (curr_node is None):
                print 'Node not found'
                return
            elif curr_node.data == del_item or curr_node == del_item:
                found = True
            else:
                prev_node, curr_node = curr_node, curr_node.next_node

        if prev_node is None: self.head = curr_node.next_node
        else: prev_node.next_node = curr_node.next_node
        self.size -= 1

    def reverse(self):
        prev, curr = None, self.head
        while(curr):
            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt

        self.head = prev

    def reverse_recursive(self, curr):
        if curr.next_node is None:
            self.head = curr
            return None

        self.reverse_recursive(curr.next_node)
        curr.next_node.next_node = curr
        curr.next_node = None

    # Todo: Implement decorators to print list

#############################
# USAGE
#############################
if __name__ == '__main__':

    print '\n-- Initialize --'
    lst = LinkedList(10)        # 10 --> *
    print lst

    print '\n-- Insert --'
    lst.append(20)          # 10 --> 20 --> *
    lst.append(30)          # 10 --> 20 --> 30 --> *
    lst.insert(15, pos=1) # 10 --> 15 --> 20 --> 30 --> *
    lst.insert(25, pos=3) # 10 --> 15 --> 20 --> 25 --> 30 --> *
    lst.insert(2)         # 2 --> 10 --> 15 --> 20 --> 25 --> 30 --> *
    lst.append(100)         # 2 --> 10 --> 15 --> 20 --> 25 --> 30 --> 100 --> *
    lst.append(500)         # 2 --> 10 --> 15 --> 20 --> 25 --> 30 --> 100 --> 500 --> *
    print lst

    print '\n-- Delete --'
    lst.delete(10)          # 2 --> 15 --> 20 --> 25 --> 30 --> 100 --> 500 --> *
    lst.delete(11111)       # Node is not present
    lst.delete(lst.head)    # 15 --> 20 --> 25 --> 30 --> 100 --> 500 --> *
    print lst

    print '\nSize of List : ' + str(lst.size)

    print '\n-- Reverse --'
    lst.reverse()
    print lst
    lst.reverse_recursive(lst.head)
    print lst















#############################
# NOTES
#############################
#
# Memory is allocated dynamically.
# Every node has random address and are linked through pointers.
# This is more useful when the number of objects to be stored is unknown and unusually large.
#
# Arrays on the other hand are limited by size. They are continuous blocks of allocation.
