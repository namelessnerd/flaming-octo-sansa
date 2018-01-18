def how_many_BSTs_helper(n, computed_bsts_list):
    if n <= 1:
       total_leaves = 1
    else:
        total_leaves = 0
        for i in range(1, n+1):
            if not computed_bsts_list[n - i]:
                computed_bsts_list[n - i] = how_many_BSTs_helper(n - i, computed_bsts_list)
            if not computed_bsts_list[i-1]:
                computed_bsts_list[i - 1] = how_many_BSTs_helper(i-1, computed_bsts_list)
            total_leaves += computed_bsts_list[i - 1] * computed_bsts_list[n - i]
            if i< n and not computed_bsts_list[i]:
                computed_bsts_list[i] = total_leaves
    return total_leaves


def how_many_BSTs(n):
    """
    Return the total number of binary search trees with n nodes
    """
    if n < 0:
        return 0
    if n <= 1:
        return 1
    total_trees = how_many_BSTs_helper(n, [0 for i in range(n)])
    return total_trees
