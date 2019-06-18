# Starting from the number 0, find the minimum number of operations
# required to reach a given positive target number.

# You can only use the following two operations:
# 1. Add 1
# 2. Double the number


def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    steps = 0

    while target != 0:
        if (target % 2) == 0:
            target //= 2
        else:
            target -= 1
        steps += 1

    return steps


print(min_operations(18))  # 6
print(min_operations(69))  # 9
