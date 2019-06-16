def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # return int(number ** 0.5)
    if number is None:
        return 0

    if number < 0:
        return 0

    if number == 0 or number == 1:
        return number

    nums = list(range(1, number))
    index = number // 2

    while (nums[index] * nums[index]) > number:
        index //= 2

    while (nums[index] * nums[index]) < number:
        index += 1

    if (nums[index] * nums[index]) == number:
        return nums[index]
    else:
        return nums[index - 1]


print(sqrt(None))  # 0
print(sqrt(-7))  # 0
print(sqrt(0))  # 0
print(sqrt(1))  # 1
print(sqrt(9))  # 3
print(sqrt(16))  # 4
print(sqrt(27))  # 5

print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
