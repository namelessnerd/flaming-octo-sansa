"""
Generate all possible expressions that evaluate to a target value

"""
def multiply(current_expr, new_number):
    current_char = len(current_expr) -1
    while (current_char > 0 and current_expr[current_char] not in ("+", "-")):
        current_char -= 1
    current_expr_without_last_number = current_expr[:current_char]
    new_expr = current_expr_without_last_number + current_expr[current_char:] + "*" + new_number
    return eval(new_expr), new_expr

def add(current_expr, new_number):
    return eval(current_expr + "+" + new_number), current_expr + "+" + new_number

def join(current_expr, new_number):
    new_expr = current_expr[:-1] + current_expr[-1] + new_number
    return eval(new_expr), new_expr

def apply_op(op_name, current_expr, new_number):
    op_method_map = {"join": join, "add": add, "multiply": multiply}
    return op_method_map[op_name](current_expr, new_number)

"""
Generate all possible expressions that evaluate to a target value

"""
def multiply(current_expr, new_number):
    current_char = len(current_expr) -1
    while (current_char > 0 and current_expr[current_char] not in ("+", "-")):
        current_char -= 1
    current_expr_without_last_number = current_expr[:current_char]
    new_expr = current_expr_without_last_number + current_expr[current_char:] + "*" + new_number
    return eval(new_expr), new_expr

def add(current_expr, new_number):
    return eval(current_expr + "+" + new_number), current_expr + "+" + new_number

def join(current_expr, new_number):
    if current_expr[-1] != 0:
        new_expr = current_expr[:-1] + current_expr[-1] + new_number
        try:
            return eval(new_expr), new_expr
        except:
            return None, None

def apply_op(op_name, current_expr, new_number):
    op_method_map = {"join": join, "add": add, "multiply": multiply}
    return op_method_map[op_name](current_expr, new_number)

def generate_all_expressions_helper(s, offset, current_exprs_dict, target):
    if offset > len(s) - 1:
        return current_exprs_dict
    next_expressions = {}
    next_int_in_input = s[offset]
    for evaluated_value in current_exprs_dict:
        # get the list of expressions that evaluate to the current value
        if evaluated_value <= target:
            current_expr_list =current_exprs_dict[evaluated_value]
            # apply the three operators to each expression in current expression list
            for current_expr in current_expr_list:
                for op in ["join", "add", "multiply"]:
                    next_value, next_expr = apply_op(op, current_expr, next_int_in_input)
                    if next_value is not None:
                        try:
                            next_expressions[next_value].append(next_expr)
                        except KeyError:
                            next_expressions[next_value] = [next_expr]
    return generate_all_expressions_helper(s, offset + 1, next_expressions, target)



def generate_all_expressions(s, target):
    if s is not None and s.isnumeric() and target is not None:
        if s == target:
            return [s]
        if len(s) > 1:
            current_exprs = {int(s[:2]) : [s[:2]], eval(s[0] + "+" + s[1]) : [s[0] + "+" + s[1], s[0] + "*" + s[1]]}
            current_exprs = generate_all_expressions_helper(s, 2, current_exprs, target)
            try:
                return current_exprs[target]
            except KeyError:
                return []
    return []

s1 = input()
s2 = input()
print(generate_all_expressions(s1, int(s2)))
