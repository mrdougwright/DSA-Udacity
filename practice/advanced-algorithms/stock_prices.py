# Solution


def max_returns(arr):
    """
    The idea is to pick two dates:
        1. buy date
        2. sell date
    We will keep track of our max profit while iterating over the list
    At each step we will make the greedy choice by choosing prices such that our profit is maximum
    """
    min_index = 0
    max_index = 1
    current_min_index = 0

    if len(arr) < 2:
        return

    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_index]:
            current_min_index = index

        # current max profit
        if arr[max_index] - arr[min_index] < arr[index] - arr[current_min_index]:
            max_index = index
            min_index = current_min_index
    max_profit = arr[max_index] - arr[min_index]
    return max_profit


print(max_returns([2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]))
