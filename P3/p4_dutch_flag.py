def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index = 0
    next_0 = 0
    next_2 = len(input_list) - 1

    while index <= next_2:
        if input_list[index] == 0:
            input_list[index] = input_list[next_0]
            input_list[next_0] = 0
            next_0 += 1
            index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[next_2]
            input_list[next_2] = 2
            next_2 -= 1
        else:
            index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function(
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
)
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

"""
The Sort 012 is a fun algorithm. Space complexity is O(1) since only a few
variables are used to keep track of indexes, and sorting is done in place. Time
complexity is O(n) since we must iterate through each item of the array to
determine whether to send a 0 to the front or a 2 to the back.

The way this algorithm works is by incrementing a front index (next_0) for found
0 integers, decrementing a rear index (next_2) for found 2 integers, and leaving
1 integers in place by incrementing the traversing index. Then you simply traverse
the array, swapping numbers when applicable.
"""
