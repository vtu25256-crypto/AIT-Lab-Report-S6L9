import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    closed_set = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g  # return path and cost

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in closed_set:
                new_g = g + cost
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # no path found

# Example graph as adjacency list: node -> [(neighbor, cost), ...]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Simple heuristic: straight-line distance (for example purposes, just zero)
def heuristic(node, goal):
    return 0  # zero heuristic turns A* into Dijkstra’s

path, cost = a_star(graph, 'A', 'D', heuristic)
print("Path:", path)
print("Cost:", cost)
