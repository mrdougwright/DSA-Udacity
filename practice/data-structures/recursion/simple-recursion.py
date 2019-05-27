def recursive(input):
    if input <= 0:
        return input
    else:
        print(input)
        return recursive(input - 1)

def power_of_2(num):
    if num == 0:
        return 1
    else:
        return 2 * power_of_2(num - 1)

"""
What the recursive call stack looks like...
power_of_2(5) # 32
    power_of_2(4) # 16
        power_of_2(3) # 8
            power_of_2(2) # 4
                power_of_2(1) # 2
                    power_of_2(0) # 1
"""

def sum_integers(num):
    # non recursive functions can be better, as in this case
    if num <= 1:
        return 1
    return num + sum_integers(num - 1)

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def reverse_string(str):
    letter = str[-1:]
    if len(str) == 0:
        return letter
    return letter + reverse_string(str[:-1])

def is_palindrome(input):
    if len(input) <= 1:
        return True
    else:
        first = input[0]
        last = input[-1]
        rest = input[1:-1]
        return (first == last) and is_palindrome(rest)

import copy
def permute(l):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item be represented by a list
    """
    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        sub_permutes = permute(l[1:])
        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j, first_element)
                perm.append(r)
    return perm


# keypad exercise
def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

# I couldn't figure this out...  :(
def keypad(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))

    keypad_str = get_characters(num % 10)
    other_nums = keypad(num // 10)
    result = []
    for char in keypad_str:
        for l in other_nums:
            result.append(char + l)

    return result

a = keypad(23)
print(a)
