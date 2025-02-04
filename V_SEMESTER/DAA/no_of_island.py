from collections import deque

def bfs(row, col, vis, grid):
    vis[row][col] = True
    n = len(grid)
    m = len(grid[0])
    
    q = deque()
    q.append((row, col))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while q:
        current_row, current_col = q.popleft()
        for del_row, del_col in directions:
            new_row = current_row + del_row
            new_col = current_col + del_col
            
            if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == "1" and not vis[new_row][new_col]:
                vis[new_row][new_col] = True
                q.append((new_row, new_col))

def num_islands(grid):
    n = len(grid)
    m = len(grid[0])
    vis = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and not vis[i][j]:
                bfs(i, j, vis, grid)
                cnt += 1    
    return cnt

if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(grid))