class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, key):
        node = self.head
        if node is None:
            self.head = self.tail = Node(key)
            self.tail.previous = self.head
            return

        self.head = Node(key)
        self.head.next = node
        node.previous = self.head

    def remove(self, key):
        if self.head is None:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def pop(self):
        old_node = self.tail
        self.tail = old_node.previous
        self.tail.next = None
        return old_node.key

    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

class LRU_Cache:
    def __init__(self, capacity):
        self.list = LinkedList()
        self.dictionary = dict()
        self.capacity = capacity

    def get(self, key):
        value = self.dictionary.get(key)
        if value:
            return value
        else:
            return -1

    def set(self, key, value):
        if self.dictionary.get(key):
            return

        if self.capacity == self.list.size():
            old_key = self.list.pop()
            del self.dictionary[old_key]

        self.list.remove(key)
        self.list.prepend(key)
        self.dictionary[key] = value


# Test Cases
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

a = our_cache.get(1)
print(a)
# returns 1

b = our_cache.get(2)
print(b)
# returns 2

c = our_cache.get(4)
print(c)
# returns -1
