from stack import *
# my attempt
import operator
def evaluate_doug_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    numbers = Stack()
    ops = {"+": operator.iadd, "-": operator.isub, "*": operator.imul, "/": operator.ifloordiv}
    # TODO: Iterate over elements
    for el in input_list:
        if el not in ["+", "-", "*", "/"]:
            numbers.push(int(el))
        else:
            a = numbers.pop()
            b = numbers.pop()
            answer = ops[el](a, b)
            numbers.push(answer)

    return answer

# correct answer
def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()

test = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
a = evaluate_post_fix(test[0])
print(a) # 22
