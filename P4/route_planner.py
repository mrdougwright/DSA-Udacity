import heapq
import math
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    visited = []
    heap = [(0, (start, start))]

    while len(heap) > 0:
        cost, (prev_dest, destination) = heapq.heappop(heap)

        if destination in visited:
            continue

        visited.append(destination)

        if destination == goal:
            return visited

        prev_path_cost = distance(
            M.intersections[prev_dest], M.intersections[destination]
        )
        for neighbor in M.roads[destination]:
            path_cost = prev_path_cost + distance(
                M.intersections[destination], M.intersections[neighbor]
            )
            estimated = distance(M.intersections[neighbor], M.intersections[goal])
            heapq.heappush(heap, (path_cost + estimated, (destination, neighbor)))
    return visited


def distance(start, end):
    # path cost is distance between two points
    return math.hypot(end[0] - start[0], end[1] - start[1])


# works:
map_40 = load_map("map-40.pickle")
shortest_path(map_40, 5, 34)  # path: [5, 16, 37, 12, 34]
# doesnt:
map_10 = load_map("map-10.pickle")
shortest_path(map_10, 2, 0)  # path: [2, 3, 0]
