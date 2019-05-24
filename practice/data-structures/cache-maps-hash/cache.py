# staircase problem
# A child is running up a staircase and can hop either 1 step, 2 steps or 3
# steps at a time. If the staircase has n steps, write a function to count
# the number of possible ways in which the child can run up the stairs.
# n == 5; answer = 13
cache = dict()

def staircase(n):
    if cache.get(n):
        output = cache[n]
    else:
        if n == 1:
            output = 1
        elif n == 2:
            output = 2
        elif n == 3:
            output = 4
        else:
            output = staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    cache[n] = output
    return output
