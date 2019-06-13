def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    lower = []
    upper = []
    output = ""
    for char in string:
        if ord(char) > 96:
            lower.append(char)
        else:
            upper.append(char)

    lower = merge_sort(lower)
    lower.reverse()
    upper = merge_sort(upper)
    upper.reverse()

    for char in string:
        if ord(char) > 96:
            output += output.join(lower.pop())
        else:
            output += output.join(upper.pop())

    return output


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid_index = len(items) // 2
    left = items[:mid_index]
    right = items[mid_index:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


test_string = "fedRTSersUXJ"
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
