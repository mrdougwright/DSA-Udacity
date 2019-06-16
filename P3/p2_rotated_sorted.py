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
        if index + 1 == len(input_list):
            # catch for sorted arrays
            index = len(input_list) // 2
            break
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


print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))  # 0
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))  # 5
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))  # 2
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))  # 3
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))  # -1

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 11, 12], 10])
test_function([[6, 7, 8, 9, 10, 11, 12], 13])
