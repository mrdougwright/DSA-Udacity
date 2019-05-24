class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        self.head = Node(value)
        self.head.next = node

    def append(self, value):
        """ Append a value to the end of the list. """
        node = self.head
        if node is None:
            self.head = Node(value)
            return

        while node.next:
            node = node.next
        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node:
            if node.value == value:
                break
            else:
                node = node.next
        return node

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        pass

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        node = self.head
        if node:
            self.head = node.next
            return node.value
        return

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return

        index = 1
        node = self.head
        while node.next and index <= pos:
            if pos == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(4)
# linked_list.insert(5, 0)
# print(linked_list.to_list())
# linked_list.insert(2, 1)
# print(linked_list.to_list())
# linked_list.insert(3, 6)
# print(linked_list.to_list())
