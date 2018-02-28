def rearrange_list(input_list, k):
    """
    Rearrange a linked list such that all nodes less than k are to the left of
    node with k and nodes greater than k are to the right
    """
    # less_list, equal_list, greater_list
    less_list = LinkedList()
    equal_list = LinkedList()
    greater_list = LinkedList()
    while input_list.next:
        current = input_list.next
        if current.val < k:
            less_list.append(current_val)
            less_list.tail = current_val
        elif current.val == k:
            equal_list.append(current_val)
            equal_list.tail = current_val
        else:
            greater_list.append(current_val)
            greater_list.tail = current_val

    if equal_list:
        try:
            less_list.tail.next = equal_list.head
        except:
            less_list = equal_list
        try:
            less_list.tail.next = greater_list.head
        except:
            pass
    else:
        return None
    return less_list
