def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    arr.sort()

    front_index = 0
    back_index = len(arr) - 1

    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:
            front_index += 1
        else:
            back_index -= 1

    return [None, None]


input = [2, 7, 11, 15]
target = 9
output = pair_sum(input, target)
print(output)
