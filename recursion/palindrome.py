def is_palindrome(input_string, left_index, right_index, input_length):
        """
        Returns if a given string is  Ignores special characters
        """
        if input_string is None:
            return False
        if right_index < left_index:
            return True
        # skip special characters when we see them
        while left_index < input_length and\
            not (input_string[left_index].isalnum()):
            left_index += 1
        while right_index >= left_index and\
            not (input_string[right_index].isalnum()):
            right_index -= 1
        if left_index <= right_index:
            return input_string[left_index].lower() == input_string[right_index].lower()\
                and is_palindrome(input_string,left_index + 1, right_index-1, input_length)
        else:
            return False

def main():
    # unit_test_cases
    unit_test_cases = {None: False, "": True, "Foo": False, "a": True,
                      "a ;;!@#!@": True, "madam": True,
                      "   ma!@#!da;;   m ": True,"abb1221bba": True,}

    for unit_test_case in unit_test_cases:
        input_length = len(unit_test_case) if unit_test_case is not None else 0
        assert(is_palindrome(unit_test_case, 0, input_length -1, input_length))\
            ==unit_test_cases[unit_test_case]
if __name__ == '__main__':
    main()
