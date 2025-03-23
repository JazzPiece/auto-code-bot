from collections import deque

def bfs_shortest_path_length(graph, start, end):
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        node, length = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == end:
                    return length + 1
                else:
                    queue.append((neighbor, length + 1))

    return -1

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print(bfs_shortest_path_length(graph, 'A', 'F'))