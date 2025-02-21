from collections import defaultdict, deque
import heapq

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# Sample graph for BFS traversal
sample_graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
print("BFS Traversal:")
bfs(sample_graph, 0)

def is_connected(graph, n):
    visited = set()
    queue = deque([0])  # Assuming the capital city is node 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return len(visited) == n

def dijkstra(graph, start, n):
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    n = 5  # Number of cities
    m = 6  # Number of roads
    sample_data = [
        (0, 1, 2),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 4),
        (2, 4, 5),
        (3, 4, 1)
    ]

    graph = defaultdict(list)
    for u, v, w in sample_data:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Assuming the roads are bidirectional

    
    if is_connected(graph, n):
        print("All cities are reachable from the capital.")
    else:
        print("Not all cities are reachable from the capital.")

    
    distances = dijkstra(graph, 0, n)
    print("Shortest distances from the capital to each city:")
    for city in range(n):
        print(f"City {city}: {distances[city]}")
