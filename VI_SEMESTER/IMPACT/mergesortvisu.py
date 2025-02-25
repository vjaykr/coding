<<<<<<< Updated upstream
#merge sort with step by step visualization
=======
#merge sort visualization
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
>>>>>>> Stashed changes

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L=arr[::mid]
        R=arr[mid::]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        
