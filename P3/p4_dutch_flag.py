def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index = 0
    next_0 = 0
    next_2 = len(input_list) - 1

    while index <= next_2:
        if input_list[index] == 0:
            input_list[index] = input_list[next_0]
            input_list[next_0] = 0
            next_0 += 1
            index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[next_2]
            input_list[next_2] = 2
            next_2 -= 1
        else:
            index += 1

    return input_list


a = sort_012([2, 2, 0])
b = sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
c = sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
d = sort_012([1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 1])
e = sort_012([1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1])
f = sort_012([])
g = sort_012([2])
h = sort_012([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

print(a)  # [0, 2, 2]
print(b)  # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
print(c)  # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print(d)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
print(e)  # [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
print(f)  # []
print(g)  # [2]
print(h)  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
