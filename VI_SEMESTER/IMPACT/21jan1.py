from collections import deque

def bfs_shortest_path(grid, start, destination):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 1
    
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == destination:
            return len(path), path
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return -1, []  # Return -1 if no path is found

# Example usage
grid = [
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
start = (0, 0)
destination = (4, 4)

length, path = bfs_shortest_path(grid, start, destination)
print("Length of the shortest path:", length)
print("Path:", path)