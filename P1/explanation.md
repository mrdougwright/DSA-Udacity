## Explanation to Problems

#### Problem 1 - LRU Cache
I think a Linked List solves the LRU Cache problem quite nicely.
The Least Recently Used item can be the trailing tail of a Linked list. If you always remove and prepend an item to the list, the head will have the most recently used item. Thus if you reach capacity, you simply pop off the tail and keep going.

The dictionary acts as a quick cached way to retrieve values from the linked list without having to actually traverse it.

Since the get and set operations are constant time, our Big O Notation is O(1).
Space complexity consists of a node list and a cache dictionary, so our Big O there is O(2n).

Big O Notation
Time: O(1)
Space: O(n)


#### Problem 2 - File Recursion
Since we have to look through every directory to check each file, the best bet is probably recursion. For my function, I simply print the path if the suffix is a match, otherwise I check if it's a directory. If it is a directory, for each file in the directory, we recursively call the function again.

The time complexity is Big O of N times the number of directories, since for each directory we call our function again. The space complexity can grow exponentially with each recursive call.

Big O Notation
Time: O(n)
Space: O(n log n)


#### Problem 3 - Huffman Encoding/Decoding
This was a difficult problem. Luckily YouTube and some fellow students helped me with understanding the algorithms involved.

My solution was to use Python's `heapq` library. To encode a string, we first count the frequency of each letter. I then make a binary tree by pulling the two smallest values off of the heap, and adding back my newly made node to the heap.

I then make a mapping from the tree, where I recursively add a '0' or a '1' to the prefix, and put that as the value for the map, where the key is the label or character from the tree.

To get the final encoding, I simply iterate over each key (or character) in the string and get the binary value from the map, and join it all together.

For decoding, we simply iterate over each "bit" in the binary string and append the value (label) while traversing the tree.

For Big O we loop over all characters, we then loop over all frequencies to make the heap. We also recurse through the tree when making the map of characters to binary code. So I believe our performance is O(n3). For space complexity we use a dictionary, a heap, and a recursive call in makeMap, giving us Big O(3n log n)

Big O Notation
Time: O(n)
Space: O(n log n)


#### Problem 4 - Users in Group
This problem is a bit unclear. I wasn't sure if it was asking us to find a user if nested within a group. But I solved for that since that could use recursion. If the user is in the group we return True. Else, for every group in the group we call our function again and search through users.

Big O Notation Time & Space: O(n)
No matter the size of users and groups, we have to search through them all recursively to find our user. We use two arrays to store our users and groups, so our Big O grows as simple multiples of these for space.


#### Problem 5 - BlockChain
Our Blockchain problem is really just a node and a linked list. Each node in the list points to the next, while also storing the hash of itself, and its previous hash.

Since we merely iterate through a linked list, and do some hashing functions, the Big O for time should be a simple O(1). And Big O for space is 1 for our hash sha and 1 for our linked list: O(2n).
Big O Notation
Time: O(1)
Space: O(n)


#### Problem 6 - Union and Intersection
The `union` function has two while loops, one for each linked list. Therefor its performance is Big O of N times 2: O(2n) or O(n).

The `intersection` function has a loop within a loop, checking for identical values in either list. It's performance is thus a bit worse at Big O of N squared: O(n**2).

In both functions I use Python's `set` function to create a unique cache list of either the union or intersection of the items in both lists. This adds another loop for iterating thru the final set, but it's effect on performance is minimal. With a linked list and a cache set, we have a space Big O of O(2n).

Big O Notation
Time: O(n**2)
Space: O(n)
