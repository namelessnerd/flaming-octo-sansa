def sum_subset(input_list, current_sum, max_sum):
    print ("Input list: {0}, Input sum: {1}".format(input_list, current_sum,))
    if input_list:
        sum_subset(input_list[1:], current_sum, max_sum)
        sum_subset(input_list[1:], current_sum + input_list[0], max_sum)
    else:
        if current_sum < max_sum:
            print ("Sum: %d" % current_sum)
        return

def cartesian(el, li):
    """
    returns the cartesian product of el and li
    """
    for item in range(len(li)):
        li.append(li[item] + el)
    return li

def generate_all_subsets(s):
    """
    Generate all subsets of a given string s
    """
    if len(s) == 1:
        return [s, ""]
    else:
        return sorted(cartesian(s[0], generate_all_subsets(s[1:])))
