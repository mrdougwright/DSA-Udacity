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

"""
Traversing the array of ints has a time complexity of O(n) and a space complexity
of O(1). We iterate through each number in a list of integers, and we set two
variables, min and max, which we will update as check the min and max of each
number. If the current number is larger than the max, it becomes the new max.
Similarly, if the current number is less than the min, it becomes the new min.
"""
