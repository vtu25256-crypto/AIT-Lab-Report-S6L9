from collections import deque

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Queue initialized with the start node

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)        # Process the node (here, just print)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

bfs(graph, 'A')
