from stack import *

def equation_checker(equation):
    # TODO: Intiate stack object
    parens = Stack()

    # TODO: Interate through equation checking parentheses
    for i in equation:
        if i == "(":
            parens.push(i)
        if i == ")":
            old_paren = parens.pop()
            if old_paren != "(":
                return False

    # TODO: Return True if balanced and False if not
    return parens.size() == 0

a = equation_checker("((32+8)∗(5/2))/(2+6)")
print(a)
print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
