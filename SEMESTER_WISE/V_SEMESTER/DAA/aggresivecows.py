def can_place_cows(stalls, n, k, min_dist):
    """Check if we can place all cows with at least `min_dist` distance apart."""
    count = 1  # First cow placed in the first stall
    last_position = stalls[0]
    
    for i in range(1, n):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            if count == k:
                return True
    return False

def aggressiveCows(stalls, k):
    """Function to find the maximum possible minimum distance."""
    stalls.sort()  # Sort the array of stall positions
    
    n = len(stalls)
    left = 1     # Minimum possible distance
    right = stalls[n-1] - stalls[0]  # Maximum possible distance
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(stalls, n, k, mid):
            result = mid  # If we can place cows with at least mid distance, try for a larger distance
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Example usage:
if __name__ == "__main__":
    stalls1 = [4, 2, 1, 3, 6]
    k1 = 2
    print(aggressiveCows(stalls1, k1))  # Output: 5
    
    stalls2 = [0, 3, 7, 10]
    k2 = 4
    print(aggressiveCows(stalls2, k2))  # Output: 3
    
