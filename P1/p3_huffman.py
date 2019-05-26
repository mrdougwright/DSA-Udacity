import sys
import heapq

def makeFreqencies(message):
    chars = dict()
    for char in message:
        if chars.get(char):
            chars[char] += 1
        else:
            chars[char] = 1
    return chars.items()

def makeTree(frequencies):
    # frequencies: list of tuples: (frequency, letter)
    heap = []
    for lf in frequencies: heapq.heappush(heap, [lf])
    while (len(heap) > 1):
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        freq0, label0 = left[0]
        freq1, label1 = right[0]
        node = [(freq0 + freq1, label0 + label1), left, right]
        heapq.heappush(heap, node)
    return heap.pop()

def makeMap(tree, map=dict(), prefix=''):
    if (len(tree) == 1):
        label, freq = tree[0]
        map[label] = prefix
    else:
        value, left, right = tree
        makeMap(left, map, prefix + "0")
        makeMap(right, map, prefix + "1")
    return map

def huffman_encoding(message):
    tree = makeTree(makeFreqencies(message))
    map = makeMap(tree)
    data = ''.join([ map[letter] for letter in message ])
    return data, tree

def huffman_decoding(data, tree):
    codeTree = tree
    decodedLetters = []

    for bit in data:
        if (bit == '0'): codeTree = codeTree[1]
        else: codeTree = codeTree[2]

        if (len(codeTree) == 1):
            label, freq = codeTree[0]
            decodedLetters.append(label)
            codeTree = tree

    return ''.join(decodedLetters)


# Test Cases
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("-------------------------------")
    a_long_sentence = "a man, a plan, a canal, panama."
    print ("The content of the data is: {}\n".format(a_long_sentence))
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_long_sentence)))
    encoded_data, tree = huffman_encoding(a_long_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

    print("-------------------------------")
    a_short_sentence = "aaaaab"
    print ("The content of the data is: {}\n".format(a_short_sentence))
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_short_sentence)))
    encoded_data, tree = huffman_encoding(a_short_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# Test Case
# The size of the data is: 69
#
# The content of the data is: The bird is the word
#
# The size of the encoded data is: 44
#
# The content of the encoded data is: 000000000010000001000000010000000000000000000010000010001000000001000000000000000010010000000000001000000100000001000000000001000010001000000001
#
# The size of the decoded data is: 69
#
# The content of the encoded data is: The bird is the word
#
# -------------------------------
# The content of the data is: a man, a plan, a canal, panama.
#
# The size of the data is: 80
#
# The size of the encoded data is: 48
#
# The content of the encoded data is: 000001000000000010000010100000001000000000000010000000010001000001010000000100000000000001000000000000100000101000001000100000001000000001000001010000010010000010000001
#
# The content of the encoded data is: a man, a plan, a canal, panama.
#
# The size of the decoded data is: 80
#
# -------------------------------
# The content of the data is: aaaaab
#
# The size of the data is: 55
#
# The content of the encoded data is: 000001
#
# The size of the encoded data is: 28
#
# The content of the encoded data is: aaaaab
#
# The size of the decoded data is: 55
