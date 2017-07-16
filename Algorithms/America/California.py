import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from LinkedList import Linked_List

i = Linked_List.LinkedList()
i.insert_begin(1993)
i.print_list()
