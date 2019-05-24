from stack import *

def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    reversed_stack = Stack()
    for i in range(stack.size()):
        item = stack.pop()
        reversed_stack.push(item)

    return reversed_stack
