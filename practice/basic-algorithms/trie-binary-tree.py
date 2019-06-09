basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def exists(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_word

t = Trie()
t.add("add")
t.add("abacus")
t.exists("add")


# Trie with Python Dictionary
import collections

class BetterTrieNode:
    def __init__(self):
        self.children = collections.defaultdict(BetterTrieNode)
        self.is_word = False

class BetterTrie:
    def __init__(self):
        self.root = BetterTrieNode()

    def add(self, word):
        node = self.root

        for char in word:
            node = node.children[char]

        node.is_word = True
        pass

    def exists(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_word
