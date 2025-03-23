from collections import deque

def bfs_shortest_path_all(graph, start):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node] - set(path):
                queue.append((neighbor, path + [neighbor]))
    
    return [path for path in [path for _, path in queue] if len(path) > 1]

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print(bfs_shortest_path_all(graph, 'A'))