from collections import deque

def bfs_cycle_detection(graph):
    for start_node in graph:
        visited = set()
        queue = deque([(start_node, None])

        while queue:
            node, parent = queue.popleft()
            if node in visited:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    queue.append((neighbor, node))

    return False

# Example usage
graph_with_cycle = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B'}
}

graph_without_cycle = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print(bfs_cycle_detection(graph_with_cycle))
print(bfs_cycle_detection(graph_without_cycle))