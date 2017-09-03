import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Node import Node as Nd

#############################
# Doubly LINKED LIST
#############################
class DoublyLinkedList(object):

    def __init__(self, data):
        new_node = Nd.DNode(data)
        self.head = new_node
        print self._printIt()

    def _printIt(self):
        curr, output = self.head, 'Head'
        while curr:
            output += ' --> [' + str(curr.data) + ":" + str(hex(id(curr))) \
                + " (Prev:" + str(hex(id(curr.prev_node))) \
                + ", Next:" + str(hex(id(curr.next_node))) + ") ]"
            curr = curr.next_node

        return output + ' --> *'

    def __str__(self):
        return self._printIt()

    # Decorator method to print the list after every operation
    # :-) This is probably overdoing, Rather call print at the end of each func
    # :-) It works, who cares !!!
    def DisplayList(thisFunc):
        def Wrapper_Func(self, *args, **kwargs):
            thisFunc(self, *args, **kwargs)
            print self._printIt()
        return Wrapper_Func

    # Insert at the begining
    @DisplayList
    def insert(self, data, pos=0 ):
        new_node = Nd.Node(data)

        # Handle node cannot be null since it is always initialized
        if pos == 0:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
            new_node.prev_node = None

        if pos > 0:
            curr = self.head
            for c in xrange(pos-1):
                if curr.next_node is None: break
                curr = curr.next_node

            new_node.next_node = curr.next_node
            new_node.prev_node = curr
            curr.next_node = new_node

    @DisplayList
    def delete(self, item):
        curr, deleted  = self.head, 0

        while curr and deleted == 0:
            if curr.data == item or curr == item:
                # first node to be deleted
                if curr.prev_node is None:
                    self.head = curr.next_node
                    self.head.prev_node = None
                    deleted = 1
                else:
                    # any other node to be deleted
                    curr.prev_node.next_node = curr.next_node
                    curr.next_node.prev_node = curr.prev_node
                    deleted = 1
            curr = curr.next_node

        if deleted == 0 : print "Node not found"

    # Todo: Reverse list

#############################
# USAGE
#############################
if __name__ == '__main__':

    print '\n-- Initialize --'
    dlst = DoublyLinkedList(100)

    print '\n-- Insert --'
    dlst.insert(30)
    dlst.insert(20)
    dlst.insert(40,1)
    dlst.delete(20)

    print '\n-- Delete --'
    dlst.delete(dlst.head)
    dlst.delete(dlst.head)
