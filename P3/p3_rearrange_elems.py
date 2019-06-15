def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    items = reverse_mergesort(input_list)
    list1 = list()
    list2 = list()

    for item in items:
        if len(list1) > len(list2):
            list2.append(str(item))
        else:
            list1.append(str(item))

    return [int("".join(list1)), int("".join(list2))]


def reverse_mergesort(items):
    if len(items) <= 1:
        return items

    index = len(items) // 2
    left = items[:index]
    right = items[index:]

    left = reverse_mergesort(left)
    right = reverse_mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]


"""
To rearrange a list of digits into two large numbers I first
reverse merge sort the list. Merge sort time complexity is O(n log(n))
and puts the largest number at the front of the list. Then I simply
iterate through the numbers, taking turns to place one in either list1 or list2,
and converting them to strings as the numbers are added to a list.
Finally, I join the list of strings and convert to ints.

The time complexity is O(2n log(n)) because we iterate through the list after
it's merged, which simplifies to O(n log(n)). The space complexity of merge sort
is O(n) with two lists created again after merging for a total of O(3n), simplified
to O(n).
"""
