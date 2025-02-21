def twoSum(nums, target):
    map = {}  # Create a dictionary to store value and index

    for i in range(len(nums)):
        complement = target - nums[i]  # Calculate the complement

        if complement in map:
            # Found a pair that adds up to the target
            return [map[complement], i]

        # Add the current number and its index to the dictionary
        map[nums[i]] = i

    # No valid pair found
    return [-1, -1]


nums = [2, 7, 11, 15]  # Example input list
target = 9  # Example target value

result = twoSum(nums, target)
if result[0] != -1:
    print("Indices of the two numbers:", result[0], ",", result[1])
    print("Numbers at those indices:", nums[result[0]], ",", nums[result[1]])
else:
    print("No valid pair found.")
