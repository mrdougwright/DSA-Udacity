import heapq
import math
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    print("shortest path called")
    graph = create_graph(M.intersections, M.roads, goal)
    heap = [(0, start)]
    shortest_path = []

    while len(heap) > 0:
        cost, vertex = min(heap)
        shortest_path.append(vertex)

        if vertex == goal:
            return shortest_path

        heap = []

        for edge_cost, neighbor in graph[vertex]:
            estimated = distance(M.intersections[neighbor], M.intersections[goal])
            heap.append((edge_cost + estimated, neighbor))

    return shortest_path


def distance(start, end):
    # path cost is distance between two points
    return math.hypot(end[0] - start[0], end[1] - start[1])


def create_graph(intersections, road_list, goal):
    adjacency_list = [list() for _ in range(len(road_list) + 1)]

    for i, intersection_list in enumerate(road_list):
        for node in intersection_list:
            path_cost = distance(intersections[i], intersections[node])
            adjacency_list[i].append((path_cost, node))

    return adjacency_list


# works:
# map_40 = load_map("map-40.pickle")
# shortest_path(map_40, 5, 34)  # path: [5, 16, 37, 12, 34]
# doesnt:
map_10 = load_map("map-10.pickle")
shortest_path(map_10, 2, 0)  # path: [2, 3, 5, 0]
