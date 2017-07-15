
def parse_rpn(expression):
    """ Evaluate a reverse polish notation"""

    stack = []

    for val in expression.split(' '):
        if val in ['-','+','*','/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '-': result = op2 - op1
            if val == '+': result = op2 + op1
            if val == '*': result = op2 * op1
            if val == '/': result = op2 / op1
            stack.append(result)
        else:
            stack.append(float(val))

    return stack.pop()

if __name__ == '__main__':

    expression = '10 3 5 + *'
    result = parse_rpn(expression)
    print result

    expression = '3 5 + 10 *'
    result = parse_rpn(expression)
    print result
