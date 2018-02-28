def flatten_list(linked_list):
    """
    Flatten a linked list where nodes can have a child pointer
    """
    head_pointer = linked_list.head
    tail_pointer = linked_list.head
    # move tail pointer to the end of the first level
    while tail_pointer.next:
        tail_pointer = tail_pointer.next
    # move head pointer to first element with child
    while not head_pointer.child:
        head_pointer = head_pointer.next
    if head_pointer != tail_pointer:
        tail_pointer.next = head_pointer.child
        head_pointer.child = None
        while head_pointer
        tail_pointer = head_pointer.child
        # CANNOT FIGURE OUT HOW TO ITERATE OVER THIS LINKED LIST
