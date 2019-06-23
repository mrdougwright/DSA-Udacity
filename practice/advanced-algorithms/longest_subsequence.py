def lcs(string_a, string_b):
    matrix = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    for char_a_i, char_a in enumerate(string_a):
        for char_b_i, char_b in enumerate(string_b):
            if char_a == char_b:
                matrix[char_a_i + 1][char_b_i + 1] = matrix[char_a_i][char_b_i] + 1
            else:
                matrix[char_a_i + 1][char_b_i + 1] = max(
                    matrix[char_a_i][char_b_i + 1], matrix[char_a_i + 1][char_b_i]
                )

    print(matrix)
    return matrix[-1][-1]
    # my fail. udacity above
    # row_index = 1
    # col_index = 1
    # for row in matrix[1:]:
    #     col_index = 1
    #     for col in row[1:]:
    #         if string_b[row_index - 1] in string_a:
    #             matrix[row_index][col_index] = matrix[row_index - 1][col_index - 1] + 1
    #         print(f"string_a[col_index]: {string_a[col_index - 1]}")
    #     print("---")
    # O(N^2) time complexity.


lcs("abcd", "bd")
