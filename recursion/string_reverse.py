def reverse_string(input_string):
    """
    Reverses an input string using recursion
    """
    try:
        if input_string is not None :
            if len(input_string)<=1:
                return input_string
            else:
                reversed_string = ""
                reversed_string += input_string[-1] + reverse_string(input_string[:-1])
                return reversed_string
        else:
            return None
    except TypeError:
        return "Cannot reverse something that is not a string"
