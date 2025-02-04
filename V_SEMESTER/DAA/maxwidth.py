def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[high]
        
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
        
    mid = (low + high) // 2
           
    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid+1, high)
    
    return min(left_min, right_min), max(left_max, right_max)

# Example usage:
arr = [7, 2, 1, 3, 4, 5, 6, 8]
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)

print("min element: ", min_val)
print("max element: ", max_val)






print(f"Minimum element: {min_val}")
print(f"Maximum element: {max_val}")
   