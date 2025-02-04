def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    j = low
    while j < high:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
        
        
arr = [4, 6, 2, 5, 7, 9, 1, 3]
quicksort(arr, 0, len(arr) - 1)
print(arr)
