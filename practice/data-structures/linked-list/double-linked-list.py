class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def to_list(self):
        list = []
        node = self.head
        while node:
            list.append(node.value)
            node = node.next
        return list

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

node = linked_list.head
while node:
    if node.previous == None:
        a = node
    else:
        a = node.previous.value
    if node.next == None:
        b = None
    else:
        b = node.next.value
    print(F"({a}) <- ({node.value}) -> ({b})")

    node = node.next
