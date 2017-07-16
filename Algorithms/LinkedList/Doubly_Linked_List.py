import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Node import Node as Nd

#############################
# Doubly LINKED LIST
#############################

class DoublyLinkedList(object):

    def __init__(self, head_node = None):
        self.head = head_node


    def insert_begin(self, data):
        if self.head is None:
            new_node = Nd.DNode(data)
            self.head = new_node
            new_node.next_node = None
            new_node.prev_node = None
