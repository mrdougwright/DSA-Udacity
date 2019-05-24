# BST
# Binary Search Tree
from binary_tree import *
from queue_helper import *

class Tree():
    def __init__(self):
        self.root = None

    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
         5
        / \
       3   10
    can use a for loop (try one or both ways)
    """
    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return

        while (True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                node.set_value(new_node.get_value())
                break
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break

    """
    define insert here (can use recursion)
    try one or both ways
    """
    def insert_with_recursion(self, value):
        if self.get_root() == None:
            self.set_root(value)
            return

        self.insert_recursively(self.get_root(), Node(value))

    def insert_recursively(self, node, new_node):
        comparison = self.compare(node, new_node)
        if comparison == 0:
            node.set_value(new_node.get_value())
        elif comparison == -1:
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        else:
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)


    def search(self, value):
        node = self.get_root()
        while node:
            if node.get_value() == value:
                return node
            elif node.get_value() < value:
                node = node.get_right_child()
            else:
                node = node.get_left_child()
        pass

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level


        return s

tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
print(tree)
