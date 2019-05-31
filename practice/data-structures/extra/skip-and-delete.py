# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    node = head
    cut_node = head
    next_node = None
    for x in range(i):
        cut_node = cut_node.next

    for x in range(i - 1):
        node = node.next

    for j in range(j):
        next_node = cut_node.next
        cut_node = cut_node.next

    node.next = next_node
    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

ll = create_linked_list([1,2,3,4,5,6])
answer = skip_i_delete_j(ll, 2, 3)
print_linked_list(answer)
