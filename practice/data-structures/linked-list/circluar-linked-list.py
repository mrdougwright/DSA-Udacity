class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not
    """
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        if slow.next == slow:
            return True

        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True
    return False

answer = iscircular(list_with_loop)
print(answer)
print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) == False else "Fail")
