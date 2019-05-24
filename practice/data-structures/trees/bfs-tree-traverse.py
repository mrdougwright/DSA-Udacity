# BFS
# Breadth First Search tree traversal
from binary_tree import *
from stack_helper import *
from queue_helper import *

# create a tree and add some nodes
tree = Tree(Node("apple"))
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
#         apple
#        /     \
#    banana    cherry
#    /
# dates

def bfs(tree):
    visit_order = list()
    queue = Queue()
    root = tree.get_root()

    queue.enq(root)
    while len(queue) > 0:
        node = queue.deq()
        visit_order.append(node.get_value())
        if node.has_left_child():
            queue.enq(node.get_left_child())
        if node.has_right_child():
            queue.enq(node.get_right_child())

    return visit_order

print(bfs(tree))
