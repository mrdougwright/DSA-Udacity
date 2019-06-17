class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, prefix=""):
        generated = self._generate_suffixes(prefix)
        return ",".join(generated)

    def _generate_suffixes(self, prefix):
        if self.is_word:
            yield prefix

        for char, node in self.children.items():
            yield from node._generate_suffixes(prefix + char)


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

print(MyTrie.find("ant").suffixes())  # ,hology,agonist,onym
print(MyTrie.find("f").suffixes())  # un,unction,actory
print(MyTrie.find("t").suffixes())  # rie,rigger,rigonometry,ripod
print(MyTrie.find("trig").suffixes())  # ger,onometry
