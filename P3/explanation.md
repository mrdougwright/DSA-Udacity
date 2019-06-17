## Explanations for Project 3 Problems

#### Problem 1 - Square Root
This problem can be solved with a simple one-liner:
```python
  int(number ** 0.5)
```

However, I believe the intent is to show how dividing a list into smaller halves
can help to solve the greater whole of the problem.

First, if the number is 0 or 1 simply return it and avoid further calculations.
Otherwise, create a list of numbers from 1 to the number passed as the argument.
Then, take the halfway point or middle of the list.

Looking at this middle number, square it and if the answer is larger than the number
keep halving your index to find a smaller result. After exiting this while loop,
do the reverse and slowly work your way up, incrementing the index by 1 until the
square is less than the number.

If the square of the found number at nums[index] equals the number, return the result.
Otherwise, return the very next number in your list, as the square root is thereby
some fraction.

The time complexity is O(log(n)) since you are halving the array as you search for
the number, and incrementing up is far less than O(n) since you are looking at a
smaller segment of the main list of numbers.
The space complexity is O(1) as you are merely making one list and a variable index
used to search for the answer.


#### Problem 2 - Rotated Array Search
First we traverse through the rotated sorted array to find the "middle" index
where the array was rotated. We use that found index to determine which half of
the array to start our pivot search. From here, we simply increment up or down
until we find the matching number. If at any point our pivot is at 0, equal to the
index, or larger than the list, we haven't found the number and we return -1.

The space complexity is O(1) because we only create placeholder variables with
no extra collections to perform our logic.

Time complexity is O(log n) because at worst case we search through half of half
of an array.


#### Problem 3 - Rearrange Digits
To rearrange a list of digits into two large numbers I first
reverse merge sort the list. Merge sort time complexity is O(n log(n))
and puts the largest number at the front of the list. Then I simply
iterate through the numbers, taking turns to place one in either list1 or list2,
and converting them to strings as the numbers are added to a list.
Finally, I join the list of strings and convert to ints.

The time complexity is O(2n log(n)) because we iterate through the list after
it's merged, which simplifies to O(n log(n)). The space complexity of merge sort
is O(n) with two lists created again after merging for a total of O(3n), simplified
to O(n).


#### Problem 4 - Sort 0, 1, 2 (Dutch National Flag)
The Sort 012 is a fun algorithm. Space complexity is O(1) since only a few
variables are used to keep track of indexes, and sorting is done in place. Time
complexity is O(n) since we must iterate through each item of the array to
determine whether to send a 0 to the front or a 2 to the back.

The way this algorithm works is by incrementing a front index (next_0) for found
0 integers, decrementing a rear index (next_2) for found 2 integers, and leaving
1 integers in place by incrementing the traversing index. Then you simply traverse
the array, swapping numbers when applicable.


#### Problem 5 - Autocomplete with Tries
Finding all the suffixes in a given Trie Dictionary was a tricky recursion problem.
But now that I know about Python's yield method, it was much easier!

To generate suffixes, we first call `find` on the Trie class to find our prefix.
Then, with the returned node, we can call `suffixes` on the TrieNode class. This
is a simple wrapper to join the yielded result of _generate_suffixes, which uses
recursion to search all nodes in children and call itself until is_word is True.

Space complexity is O(1), since no new objects are created in memory, besides
a simple variable `generated`. The time complexity is O(n), since to find all
the suffixes, we have to traverse all nodes in the tree.


#### Problem 6 - Unsorted Integer Array
Traversing the array of ints has a time complexity of O(n) and a space complexity
of O(1). We iterate through each number in a list of integers, and we set two
variables, min and max, which we will update as check the min and max of each
number. If the current number is larger than the max, it becomes the new max.
Similarly, if the current number is less than the min, it becomes the new min.


#### Problem 7 - HTTP Router with Trie
The RouteTrieNode and RouteTrie are similar to a regular TrieNode and Trie respectively.
The main difference is the addition of a handler to the TrieNode. In the main Router,
we initialize our routes with a RouteTrie, adding a "/" root route and our default
`not found` route handler. To add a handler or lookup a route, we simply call on
the familiar functions of RouteTrie `insert` and `find` passing a list of paths
already split by the backslash ("/").

The time and space complexity is negligible for our Route Trie. This is because
a url will never be longer than a few hundred characters at most. Our `add_handler`
splits a route by its words ("/") and simply traverses the node's children for any
matches before inserting the new path. The `lookup` function also splits the route
into a list of paths, using each path to traverse the node children in search of a match.

Therefore you get a O(1) space and time complexity, since the size of the input
doesn't drastically change either the space used for creating a Route Trie, nor
the time needed to lookup a route.
