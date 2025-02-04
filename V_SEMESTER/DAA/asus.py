# 1. Prime Number Check
# python
# Copy code
def is_prime(num):
    """Check if the given number is a prime number."""
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, it's prime

# Example usage
print(is_prime(11))  # Output: True




# 2. Search Insert Position
# python
# Copy code
def search_insert(nums, target):
    """Return the index of target in nums, or where it would be if not found."""
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # The correct insert position

# Example usage
print(search_insert([1, 3, 5, 6], 5))  # Output: 2




# 3. Minimum Candies Distribution
# python
# Copy code
def min_candies(ratings):
    """Distribute candies to children based on their ratings."""
    n = len(ratings)
    if n == 0:
        return 0

    candies = [1] * n  # Start with 1 candy for each child

    # Left to right: Ensure right neighbor gets more if higher rating
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left: Ensure left neighbor gets more if higher rating
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)  # Total candies distributed

# Example usage
print(min_candies([1, 0, 2]))  # Output: 5





# 4. Largest Minimum Distance for Cows
# python
# Copy code
def can_place_cows(stalls, cows, distance):
    """Check if cows can be placed with at least 'distance' apart."""
    count, last_position = 1, stalls[0]
    for stall in stalls[1:]:
        if stall - last_position >= distance:
            count += 1
            last_position = stall
        if count == cows:
            return True
    return False

def largest_min_distance(stalls, cows):
    """Return the largest minimum distance between cows."""
    stalls.sort()  # Sort the stall positions
    left, right = 1, stalls[-1] - stalls[0]  # Set search boundaries
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(stalls, cows, mid):
            result = mid  # Found a valid configuration
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example usage
print(largest_min_distance([1, 2, 8, 4, 9], 3))  # Output: 3





# 5. Cycle Detection in Graph
# python
# Copy code
def has_cycle(graph):
    """Check if the undirected graph contains a cycle."""
    visited = set()

    def dfs(node, parent):
        visited.add(node)  # Mark the node as visited
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):  # Recurse to check neighbors
                    return True
            elif neighbor != parent:  # Found a back edge
                return True
        return False

    for v in graph:
        if v not in visited:  # Start DFS from unvisited nodes
            if dfs(v, -1):
                return True
    return False

# Example usage
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
print(has_cycle(graph))  # Output: True




# 6. Critical Connections in Network
# python
# Copy code
def critical_connections(n, connections):
    """Return all critical connections in the network."""
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    ids = [0] * n  # To store ids of nodes
    low = [0] * n  # To track the lowest reachable node
    visited = [False] * n
    bridges = []
    id_counter = 0

    def dfs(at, parent):
        nonlocal id_counter
        visited[at] = True
        id_counter += 1
        ids[at] = low[at] = id_counter

        for to in graph[at]:
            if to == parent:
                continue
            if not visited[to]:
                dfs(to, at)
                low[at] = min(low[at], low[to])
                if ids[at] < low[to]:  # Found a bridge
                    bridges.append([at, to])
            else:
                low[at] = min(low[at], ids[to])

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)

    return bridges

# Example usage
print(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))  # Output: [[1, 3]]





# 7. Number of Islands
# python
# Copy code
def num_islands(grid):
    """Count the number of islands in a grid."""
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark the land as visited
        # Explore neighbors
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1  # Found an island

    return count

# Example usage
print(num_islands([["1","1","0","0","0"],
                   ["1","1","0","0","0"],
                   ["0","0","1","0","0"],
                   ["0","0","0","1","1"]]))  # Output: 3






# 8. Rotting Oranges
# python
# Copy code
from collections import deque

def min_time_to_rot_oranges(grid):
    """Determine the minimum time required to rot all oranges."""
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    queue = deque()

    # Count fresh oranges and enqueue rotten ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                queue.append((r, c))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minutes = 0

    # BFS to spread rot
    while queue and fresh:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot the orange
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1  # Increment time after each level

    return minutes if fresh == 0 else -1  # If all fresh oranges rotted

# Example usage
print(min_time_to_rot_oranges([[2,1,1],[1,1,0],[0,1,1]]))  # Output: 4



# 9. Minimum Edit Distance
# python
# Copy code
def min_edit_distance(str1, str2):
    """Calculate minimum edits to convert str1 into str2."""
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize dp table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Insert all characters of str2
            elif j == 0:
                dp[i][j] = i  # Remove all characters of str1
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  # Insert, Remove, Replace

    return dp[m][n]  # Minimum operations required

# Example usage
print(min_edit_distance("horse", "ros"))  # Output: 3





# 10. Minimum Path Sum
# python
# Copy code
def min_path_sum(grid):
    """Calculate the minimum path sum from top-left to bottom-right."""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue  # Starting point
            top = grid[r - 1][c] if r > 0 else float('inf')
            left = grid[r][c - 1] if c > 0 else float('inf')
            grid[r][c] += min(top, left)  # Take the min from top or left

    return grid[rows - 1][cols - 1]  # Bottom-right corner value

# Example usage
print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7




# 11. Remove K Digits
# python
# Copy code
def remove_k_digits(num, k):
    """Return the smallest possible integer after removing k digits."""
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()  # Remove larger digits
            k -= 1
        stack.append(digit)
    
    # Remove any remaining digits from the end
    final_num = ''.join(stack[:-k]) if k else ''.join(stack)
    
    # Remove leading zeros and return result
    return final_num.lstrip('0') or '0'

# Example usage
print(remove_k_digits("1432219", 3))  # Output: "1219"



# 12. Unique Paths
# python
# Copy code
def unique_paths(m, n):
    """Return the number of unique paths from top-left to bottom-right."""
    dp = [[1] * n for _ in range(m)]  # Initialize dp table

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Paths from top and left

    return dp[m - 1][n - 1]  # Bottom-right value

# Example usage
print(unique_paths(3, 7))  # Output: 28