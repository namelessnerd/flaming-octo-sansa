special_chars = [".", ",", "!", ";", ":", "\\", "-", '"']
def palindrome_helper(s, left_index, right_index, string_length):
    if s[left_index] in special_chars:
        left_index += 1
        return palindrome_helper(s, left_index, right_index, string_length)
    if s[right_index] in special_chars:
        right_index -= 1
        return palindrome_helper(s, left_index, right_index, string_length)
    if s[left_index] == s[right_index]:
        if (string_length - abs(right_index)) >= left_index:
            left_index += 1
            right_index -= 1
            return palindrome_helper(s, left_index, right_index, string_length)
        else:
            return 1


def is_palindrome(s):
    """
    Return if a string is palindrome, ignoring punctuation marks, using recursion
    """
    # term_char
    return 1 if palindrome_helper(s, 0, -1, len(s)) else 0

def main():
    # input_string
    input_string = input()
    print (is_palindrome(input_string))



if __name__ == '__main__':
    main()
