from collections import deque

def bfs_shortest_path_improved(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node] - set(path):
                if neighbor == end:
                    yield path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

for path in bfs_shortest_path_improved(graph, 'A', 'F'):
    print(path)