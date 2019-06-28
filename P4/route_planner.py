import heapq
import math
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    frontier = [(0, start)]

    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1]

        if node == goal:
            break

        for neighbor in M.roads[node]:
            path_cost = distance(M.intersections[node], M.intersections[neighbor])
            new_cost = cost_so_far[node] + path_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))
                came_from[neighbor] = node

    return best_route(came_from, start, goal)


def distance(start, end):
    # path cost is distance between two points
    return math.hypot(end[0] - start[0], end[1] - start[1])


def best_route(came_from, start, goal):
    # traverse backwards to find optimal path
    node = goal
    path = []
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    print(path)
    return path


# example 1
map_40 = load_map("map-40.pickle")
shortest_path(map_40, 8, 24)  # path: [8, 14, 16, 37, 12, 17, 10, 24]
# example 2
map_10 = load_map("map-10.pickle")
shortest_path(map_10, 2, 0)  # path: [2, 3, 5, 0]
