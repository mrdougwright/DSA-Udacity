# DFS
# Depth First Search tree traversal
from binary_tree import *
from stack_helper import *

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

# pre order traversal
def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

# in-order traversal
def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node.get_value())

    traverse(root)
    return visit_order
