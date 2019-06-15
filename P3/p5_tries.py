class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=""):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        if suffix in self.children:
            return self._merge_suffixes(self.children[suffix])
        else:
            return None

    def _merge_suffixes(self, node):
        my_list = []

        if len(node.children) is not 0:
            for char, node in node.children.items():
                for el in self._merge_suffixes(node):
                    my_list.append(char + el)
        else:
            my_list.append("")

        return my_list


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

"""
This version differs slightly from the notebook, where you can gather suffixes
by sending in an explicit node. For example:
>>> MyTrie.root.suffixes("a")
['nthology', 'ntagonist', 'ntonym']

Finding all the suffixes in a given Trie Dictionary was a tricky recursion problem.
First, I knew that my main `suffixes` function would call a secondary recursive
function: _merge_suffixes. Inside this function, I create a new empty list. Then
if the node has children, I iterate through it's items (a char and a node). For
each of these iterations, I call the function again, appending the list with the
char and the returned partial array list form _merge_suffixes.

As the call stack resolves, the elements from each _merge_suffixes' call get
appended to the char in the for loop, working their way back up so that all suffixes
are returned in a list.

Space complexity is O(n), since we create a new array for every node in children.
Time complexity is also O(n), since we traverse all children while building the
suffixes.
"""
