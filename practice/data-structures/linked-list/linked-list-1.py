# Implement a Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def traverse_list(self):
        print(self.value)
        if self.next:
            self.next.traverse_list()

def create_linked_list(values):
    if not values:
        return None
    head = node = Node(values[0])
    for num in values[1:]:
        node.next = Node(num)
        node = node.next
    return head


head = create_linked_list([2,1,4,3,5])
head.traverse_list()
