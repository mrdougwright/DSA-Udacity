def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
    ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]
    for num in ints:
        if num > max:
            max = num
        if num < min:
            min = num

    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print(get_min_max([1]))  # (1, 1)
print(get_min_max([10, 5, 6, 0, 12, 8]))  # (0, 12)
print(get_min_max([5, 6, 12, 80, 8]))  # (5, 80)
print(get_min_max([1, 22, 5, 6, 0, 12, 8, 9, 4, 4, 2, 20]))  # (0, 22)
