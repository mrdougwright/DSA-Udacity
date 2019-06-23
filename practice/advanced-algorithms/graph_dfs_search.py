from graph import *


def dfs_search(root_node, search_value):
    visited = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                stack.append(child)

        # print([x.value for x in visited])


assert nodeA == dfs_search(nodeS, "A")


def dfs_recursion_start(start_node):
    visited = {}

    def dfs_recursion(node, visited):
        if node == None:
            return False

        visited[node.value] = True
        print(node.value)

        for each in node.children:
            if each.value not in visited:
                dfs_recursion(each, visited)

    dfs_recursion(start_node, visited)
