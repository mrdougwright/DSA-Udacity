from graph import *


def bfs_search(root_node, search_value):
    visited = []
    queue = [root_node]

    while len(queue) > 0:
        node = queue.pop(0)
        visited.append(node)

        if node.value == search_value:
            return node

        for child in node.children:
            if child not in visited:
                queue.append(child)
