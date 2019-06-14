def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # return int(number ** 0.5)

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


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")


"""
This problem can be solved with a simple one-liner: int(number ** 0.5)
However, I believe the intent is to show how dividing a list into smaller halves
can help to solve the greater whole of the problem.

First, if the number is 0 or 1 simply return it and avoid further calculations.
Otherwise, create a list of numbers from 1 to the number passed as the argument.
Then, take the halfway point or middle of the list.

Looking at this middle number, square it and if the answer is larger than the number
keep halving your index to find a smaller result. After exiting this while loop,
do the reverse and slowly work your way up, incrementing the index by 1 until the
square is less than the number.

If the square of the found number at nums[index] equals the number, return the result.
Otherwise, return the very next number in your list, as the square root is thereby
some fraction.

The time complexity is O(log(n)) since you are halving the array as you search for
the number, and incrementing up is far less than O(n) since you are looking at a
smaller segment of the main list of numbers.
The space complexity is O(1) as you are merely making one list and a variable index
used to search for the answer.
"""
