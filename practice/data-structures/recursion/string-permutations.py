def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    return _permutations(string, 0)

def _permutations(string, index):
    if index >= len(string):
        return [""]

    small_output = _permutations(string, index + 1)
    # print(small_output)
    output = list()
    current_char = string[index]

    for perm in small_output:
        for index in range(len(small_output[0]) + 1):
            new_perm = perm[0: index] + current_char + perm[index:]
            output.append(new_perm)
    return output



# Test Cases
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

# string = 'ab'
# solution = ['ab', 'ba']
# test_case = [string, solution]
# test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)
