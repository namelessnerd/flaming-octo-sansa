
def stack_push(element, stack, current_min):
    """
    Implements min operation on a stack
    Args:
    element
    stack (stack)
    Returns:
    Min element
    """
    if element <= current_min:
        try:
            stack.push(2*element - current_min)
            current_min = element

def pop(stack):
    val = stack.pop()
    if val < current_min:
        ret_val = current_min
        current_min = 2*current_min - val
        return ret_val
    return val
