def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    lower_str1 = "".join(str1.split()).lower()
    lower_str2 = "".join(str2.split()).lower()

    if sorted(lower_str1) == sorted(lower_str2):
        return True

    return False

# anagram_checker('Dormitory','Dirty room')

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    word_list = our_string.split(' ')

    for index in range(len(word_list)):
        word_list[index] = word_list[index][::-1]

    return " ".join(word_list)


def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    if len(str1) != len(str2):
        return None

    lower_str1 = str1.lower()
    lower_str2 = str2.lower()
    matches = 0
    string_length = len(lower_str1)

    for i in range(string_length):
        if (lower_str1[i] == lower_str2[i]):
            matches += 1

    return string_length - matches
