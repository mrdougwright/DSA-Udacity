def pair_sum_to_zero(input_list, target):
    cache = {}
    for index, item in enumerate(input_list):
        if target - item in cache:
            return [cache[target - item], index]
        cache[item] = index

def longest_consecutive_subsequence(input_list):
    dict = {}

    for index, element in enumerate(input_list):
        dict[element] = index

    max_length = -1
    starts_at = len(input_list)

    for index, el in enumerate(input_list):
        current_starts = index
        current_count = 1
        current = el + 1

        while current in dict and dict[current] > 0:
            current_count += 1
            dict[current] = -1
            current += 1

        current = el - 1
        while current in dict and dict[current] > 0:
            current_starts = dict[current]
            current_count += 1
            dict[current] = -1
            current -= 1

        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]
    return [el for el in range(start_element, start_element + max_length)]
