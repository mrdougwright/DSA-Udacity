def binary_search(array, target):
    middle = len(array) // 2
    while len(array) > 1:
        if target < array[middle]:
            array = array[:middle]
            middle = len(array) // 2
        else:
            array = array[middle:]
            middle = len(array) // 2

    if target == array[0]:
        return target
    else:
        return "Not found"

# my recursive binary search function
def binary_search_recursive(array, target):
    middle = len(array) // 2
    if target == array[middle]:
        return middle
    elif len(array) == 1:
        return -1
    elif target < array[middle]:
        array = array[:middle]
        return binary_search_recursive(array, target)
    else:
        array = array[middle:]
        return binary_search_recursive(array, target)


# Udacity's recursive binary search function; doesn't find first index
def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):
    index = binary_search_recursive(source, target)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


def contains(target, source):
    return recursive_binary_search(target, source) is not None
    # for item in source:
    #     if item == target:
    #         return True
    #     else:
    #         continue
    # return False


def first_and_last_index(arr, number):
    index = find_first(number, arr)
    last_index = index
    while arr[last_index] == number:
        last_index += 1
    return [index, last_index - 1]

ans = first_and_last_index([0, 1, 2, 2, 3, 3, 3, 4, 5, 6], 3)
print(ans)
