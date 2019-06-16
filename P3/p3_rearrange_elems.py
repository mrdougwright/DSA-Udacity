def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list

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

print(rearrange_digits([4, 6, 2, 5, 9, 8]))  # [964, 852]]
print(rearrange_digits([2, 1]))  # [2, 1]
print(rearrange_digits([42]))  # [42]
print(rearrange_digits(None))  # None
print(rearrange_digits([2, 1, 9, 7, 8]))  # [971, 82]
print(rearrange_digits([8, 7, 6, 4, 2, 1]))  # [862, 741]


def rearrange_digits_udacity_solution(input_list):
    num1 = 0
    num2 = 0

    digit_place = 1  # ones, tens, hundreds etc. places
    flag = 1  # 1 for num1, 2 for num2

    for digit in range(10):
        for num in input_list:
            if num == digit:
                if flag == 1:
                    num1 += digit * digit_place
                    flag = 2
                else:
                    num2 += digit * digit_place
                    flag = 1

                    # change digit place (like, tens to hundreds)
                    digit_place = 10 * digit_place

    return [num1, num2]
