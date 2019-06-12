# Merge Sort
# multiply number of iterations by number of comparisons
# O(n log(n) )
# space complexity is more than bubble sort (new arrays)
def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid_index = len(items) // 2
    left = items[:mid_index]
    right = items[mid_index:]

    # Call mergesort recursively with the left and right half
    print(f"left: {left}")
    print(f"right: {right}")
    print("--------------")
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
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


mergesort([5, 2, 3, 1, 8, 7, 6])
