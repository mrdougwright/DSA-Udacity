# quick sort
# pivot is 2. Compare 8 < 2 ?
# 8 moves to last index; 2 to 2nd to last, 10 to first.
# |----------------\
[8, 3, 1, 7, 0, 10, 2]
# \_____________/ \_/
# Udacity Solution:
def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)


items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)
