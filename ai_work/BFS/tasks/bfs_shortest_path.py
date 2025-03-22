from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
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

for path in bfs_shortest_path(graph, 'A', 'F'):
    print(path)