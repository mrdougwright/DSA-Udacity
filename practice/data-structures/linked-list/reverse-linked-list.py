# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

def reverse(list):
    """Reverse the inputted linked list"""
    rlist = LinkedList()
    node = list.head
    while node:
        new_node = node
        node = node.next

        new_node.next = rlist.head
        rlist.head = new_node
    return rlist

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

print(llist)
print(reverse(llist))
