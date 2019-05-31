def print_integers(n):
    # TODO: Complete the function so that it uses recursion
    # to print all integers from n to 1
    if n < 1:
        return
    else:
        print(n)
    print_integers(n - 1)

print_integers(5)
# http://www.pythontutor.com/
