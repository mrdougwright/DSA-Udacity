def deep_reverse(arr):
    reversed_list = list()
    for item in arr:
        if type(item) is int:
            reversed_list = [item] + reversed_list
        if type(item) is list:
            nested_list = deep_reverse(item)
            reversed_list = [nested_list] + reversed_list
    return reversed_list


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)
