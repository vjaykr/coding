def NGE(arr):
    # Create an empty stack and push the first element of the array to it
    stack = []
    stack.append(arr[0])
    
    # Traverse the array from the second element
    for i in range(1, len(arr)):
        next = arr[i]
        if len(stack) > 0:
            element = stack.pop()
            while element < next:
                # Print the next greater element and update the element to the top of the stack
                print(str(element) + "-->  " + str(next))
                if len(stack) == 0:
                    break
                element = stack.pop()
            if element > next:
                stack.append(element)
        stack.append(next)
    
    # If there are no more elements in the array, pop the remaining elements from the stack and print -1
    while len(stack) > 0:
        element = stack.pop()
        next = -1
        print(str(element) + "-->  " + str(next))
      
arr = [13,32,43,54]
NGE(arr)
