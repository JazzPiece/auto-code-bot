from collections import deque

def bfs_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            queue = deque([node])

            while queue:
                curr_node = queue.popleft()
                if curr_node not in visited:
                    component.append(curr_node)
                    visited.add(curr_node)
                    queue.extend(graph[curr_node] - visited)

            components.append(component)
    
    return components

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'},
    'G': {'H'},
    'H': {'G'}
}

print(bfs_connected_components(graph))