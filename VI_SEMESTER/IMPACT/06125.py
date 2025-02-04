def binary_search_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  
            
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  
            
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def count_occurrences(arr, target):
    first_occurrence = binary_search_first_occurrence(arr, target)
    if first_occurrence == -1:
        return 0
    last_occurrence = binary_search_last_occurrence(arr, target)
    return last_occurrence - first_occurrence + 1

# Example usage:
sorted_array = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
target = 2
count = count_occurrences(sorted_array, target)
print(f"Count of {target}: {count}")
