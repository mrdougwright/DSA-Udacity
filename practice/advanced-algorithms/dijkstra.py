from dijkstra_graph import *
import math


def dijkstra(start_node, end_node):
    shortest_path = {}
    distance_dict = {node: math.inf for node in graph.nodes}
    distance_dict[start_node] = 0

    while distance_dict:
        node, distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        shortest_path[node] = distance_dict.pop(node)

        for edge in node.edges:
            if edge.node in distance_dict:
                new_node_distance = distance + edge.distance
                if new_node_distance < distance_dict[edge.node]:
                    distance_dict[edge.node] = new_node_distance

    return shortest_path[end_node]


print(
    "Shortest Distance from {} to {} is {}".format(
        node_u.value, node_y.value, dijkstra(node_u, node_y)
    )
)
# def dijkstra(start_node, end_node):
# my fail attempt
# distance = 0
# queue = [start_node]
#
# while len(queue) > 0:
#     node = queue.pop(0)
#
#     if node == end_node:
#         return distance
#
#     next_edge = node.edges[0]
#     for edge in node.edges:
#         if edge.distance < next_edge.distance:
#             next_edge = edge
#
#     distance += 1
#     queue.append(next_edge.node)
#     print([q.value for q in queue])
