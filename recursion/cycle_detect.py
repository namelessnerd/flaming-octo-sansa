"""
Detects cycles in a linked list
"""
class Node(object):
    """
    Class to represent a node in a linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def add_to_list(last_node, new_node):
    """
    Add new node to the list by sending the last node
    Args:
    last_node (Node)
    new_node (Node)
    """
    last_node.next = new_node

def detect_cycles(start_node):
    """
    Detect a cycle given a start node
    Args:
    start_node (Node)
    Returns:
    (bool) - True if cycle
    """
    # slow_pointer (Node)
    # fast_pointer (Node)
    slow_pointer, fast_pointer = None, None
    while (not fast_pointer and slow_pointer!= fast_pointer):
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
        fast_pointer = fast_pointer.next
    if fast_pointer:
        return True

def find_cycle_start(start_node, cycle_node):
    """
    Finds the start of the cycle
    Args:
    start_node (Node)
    cycle_node (Node)
    Returns:
    (Node)
    """
    cycle_length = 0
    # cycle_start_copy
    cycle_start_copy = cycle_node
    while not(start_node == cycle_node):
        start_node = start_node.next
        cycle_node = cycle_node.next
        cycle_length += 1
    while not(cycle_node != cycle_start_copy):
        cycle_code = cycle_code.next
        cycle_length += 1
    return start_node, cycle_length
