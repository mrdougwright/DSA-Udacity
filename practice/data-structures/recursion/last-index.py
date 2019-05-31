def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    if len(arr) <= 0:
        return -1

    index = len(arr) - 1
    if arr[index] == target:
        return index
    else:
        return last_index(arr[:-1], target)
