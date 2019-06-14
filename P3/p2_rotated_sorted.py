def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    index = 0
    while input_list[index] < input_list[index + 1]:
        index += 1
    index += 1

    if number in input_list[:index]:
        pivot = len(input_list[:index]) // 2
    else:
        pivot = index + (len(input_list[index:]) // 2)

    while input_list[pivot] != number:
        if pivot == index:
            return -1
        if input_list[pivot] < number:
            pivot += 1
        else:
            pivot -= 1

        if pivot < 0 or pivot >= len(input_list):
            return -1

    return pivot


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


"""
First we traverse through the rotated sorted array to find the "middle" index
where the array was rotated. We use that found index to determine which half of
the array to start our pivot search. From here, we simply increment up or down
until we find the matching number. If at any point our pivot is at 0, equal to the
index, or larger than the list, we haven't found the number and we return -1.

The space complexity is O(1) because we only create placeholder variables with
no extra collections to perform our logic.

Time complexity is O(log n) because at worst case we search through half of half
of an array.
"""
