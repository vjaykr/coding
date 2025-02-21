from collections import deque

def contains_cycle(graph, start_node):
    visited = set()
    parent = {}
    q = deque([(start_node, -1)])

    while q:
        node, prev_node = q.popleft()
        visited.add(node)
        parent[node] = prev_node

        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append((neighbor, node))
            elif neighbor != prev_node:
                return True

    return False

# Example usage
dict_a = {
    1: [2, 3],
    2: [1, 5],
    3: [1, 4, 6],
    4: [3],
    5: [2, 7],
    6: [3, 7],
    7: [5, 6]
}

start_node = 1
has_cycle = contains_cycle(dict_a, start_node)
print(f"The graph contains a cycle: {has_cycle}")