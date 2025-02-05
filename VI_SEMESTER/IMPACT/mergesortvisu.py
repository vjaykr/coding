def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Print splitting step
        print(f"\nSplitting: {arr} → Left: {left}, Right: {right}")
        
        # Recursively sort left and right
        merge_sort(left)
        merge_sort(right)
        
        # Merge the sorted halves
        print(f"\nMerging: Left {left} + Right {right} → Original array")
        i = j = k = 0
        
        # Compare elements and merge
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                print(f"  Placing left[{i}] ({left[i]}) → position {k}")
                arr[k] = left[i]
                i += 1
            else:
                print(f"  Placing right[{j}] ({right[j]}) → position {k}")
                arr[k] = right[j]
                j += 1
            k += 1
        #its working
        # Copy remaining elements from left
        while i < len(left):
            print(f"  Copying remaining left[{i}] ({left[i]}) → position {k}")
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy remaining elements from right
        while j < len(right):
            print(f"  Copying remaining right[{j}] ({right[j]}) → position {k}")
            arr[k] = right[j]
            j += 1
            k += 1
        
        # Show array after merging
        print(f"After merging: {arr}")
    return arr

# Test the implementation
if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)
    merge_sort(sample_array)
    print("\nFully sorted array:", sample_array)