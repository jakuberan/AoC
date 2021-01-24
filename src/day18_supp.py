def evaluate_math_noprec(x):
    """
    Evaluates math with no precedence
    """
    op = ""
    num = None
    while len(x) > 0:
        c = x.pop(0)
        if c == "+":
            op = "+"
        elif c == "*":
            op = "*"
        elif c == "(":
            x, res = evaluate_math_noprec(x)
            if op == "+":
                num += res
            elif op == "*":
                num *= res
            else:
                num = res
        elif c == ")":
            return x, num
        elif num is None:
            num = int(c)
        else:
            if op == "+":
                num += int(c)
            elif op == "*":
                num *= int(c)
    return x, num


def doper(nums, ops, final=False):
    """
    Perform the operation
    """
    # Evaluate if there are 3 terms
    if len(nums) == 3:
        if ops[1] == "+":
            nums, ops = [nums[0], nums[1] + nums[2]], [ops[0]]
        else:
            if ops[0] == "+":
                nums = [nums[0] + nums[1], nums[2]]
            else:
                nums = [nums[0] * nums[1], nums[2]]
            ops = [ops[1]]

    # Given the state (final / non-final), evaluate the rest
    if final:
        if len(nums) == 2:
            if ops[0] == "+":
                nums = [nums[0] + nums[1]]
            else:
                nums = [nums[0] * nums[1]]
        return nums[0], []
    else:
        return nums, ops


def evaluate(x):
    """
    Evaluates math with precedence
    """
    op = []
    num = []
    while len(x) > 0:
        c = x.pop(0)
        if c in ["+", "*"]:
            op.append(c)
        elif c == "(":
            x, res = evaluate(x)
            num.append(res)
            num, op = doper(num, op)
        elif c == ")":
            return x, doper(num, op, final=True)[0]
        else:
            num.append(int(c))
            num, op = doper(num, op)
    return x, doper(num, op, final=True)[0]
