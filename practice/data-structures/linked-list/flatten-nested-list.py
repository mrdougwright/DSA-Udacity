# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_alt = list1.head
    list2_alt = list2.head
    while list1_alt is not None or list2_alt is not None:
        if list1_alt is None:
            merged.append(list2_alt)
            list2_alt = list2_alt.next
        elif list2_alt is None:
            merged.append(list1_alt)
            list1_alt = list1_alt.next
        elif list1_alt.value <= list2_alt.value:
            merged.append(list1_alt)
            list1_alt = list1_alt.next
        else:
            merged.append(list2_alt)
            list2_alt = list2_alt.next
    return merged


class NestedLinkedList(LinkedList):
    def flatten(self):
        nodes = self._flatten(self.head)
        arr = []
        node = nodes.head
        while node:
            arr.append(node)
            node = node.next
        return arr

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

flattened = nested_linked_list.flatten()
print(flattened)
