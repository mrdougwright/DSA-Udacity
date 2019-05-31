def duplicate_number(arr):
    nums = set()
    for num in arr:
        if num in nums:
            return num
        else:
            nums.add(num)
    return -1

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

# Udacity (wrong) solution:
def u_duplicate_number(arr):
    current_sum = 0
    expected_sum = 0

    for num in arr:
        current_sum += num

    for i in range(len(arr) - 1):
        expected_sum += i
    return current_sum - expected_sum
