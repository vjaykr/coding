import heapq

def dijkstra(graph, start, end, traps):
    n = len(graph)
    distances = {node: float('infinity') for node in range(n)}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == end:
            return current_distance
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            if neighbor in traps:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return float('infinity')

def find_shortest_safe_path(n, edges, traps, start, treasure):
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    shortest_distance = dijkstra(graph, start, treasure, traps)
    if shortest_distance == float('infinity'):
        return "No safe path exists."
    return shortest_distance

# Example usage
n = 6
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
]
traps = [3]
start = 0
treasure = 5

print(find_shortest_safe_path(n, edges, traps, start, treasure))