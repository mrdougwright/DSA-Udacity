class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, prefix=""):
        # ensure prefix exists
        index = 0
        node = self
        while index < len(prefix):
            char = prefix[index]
            if char not in node.children:
                return -1
            index += 1
            node = node.children[char]

        return self._merge_words(node, [])

    def _merge_words(self, node, words):
        word = ""
        root_node = node

        while len(node.children) >= 0:
            if len(node.children) > 0:
                char = next(iter(node.children.keys()))

            if node.is_word:
                node.is_word = False
                words.append(word)
                node = root_node
                word = ""
            elif len(node.children) > 0:
                word += char
                node = node.children[char]
            else:
                break

        return words


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]

        return node


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.root.suffixes("f"))  # ['nthology', 'ntagonist', 'ntonym']
print(MyTrie.root.suffixes("b"))  # -1
print(MyTrie.root.suffixes("fu"))  # ['unction', 'actory']
print(MyTrie.root.suffixes("t"))  # ['rie', 'rigger', 'rigonometry', 'ripod']
