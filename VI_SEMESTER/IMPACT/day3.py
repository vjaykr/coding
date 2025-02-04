#dictonary
# key value pair
# key is unique
# value can be duplicate
# key is immutable
# value is mutable
# key can be string, number, tuple
# value can be any data type

d = {}
print(d)
d['name'] = 'John'
print(d)
d['age'] = 25
print(d)
d['city'] = 'New York'
print(d)

d1=d.copy()
print(d1)

print(d.get('name'))
print(d.get('age'))
print(d.get('city'))

print(d.fromkeys('name'))
for i in d:
    print(i)

print(d.items())

print(d.keys())

print(d.pop('name'))


def word_frequency_counter(s):
    words = s.lower().split()
    
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Example usage
input_string = "hello world Hello"
result = word_frequency_counter(input_string)
print(result)




def find_missing_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    complete_set = set(range(n + 1))
    nums_set = set(nums)
    missing_numbers = list(complete_set - nums_set)
    return missing_numbers

# Test case 1
assert find_missing_numbers([3, 0, 1]) == [2, 4]
# Test case 2
assert find_missing_numbers([0, 1]) == [2, 3]
# Test case 3
assert find_missing_numbers([9, 6, 4, 2, 3, 5, 7, 0, 1]) == [8, 10]







def spiral_order(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                resultKO.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

# Test case 1
assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
# Test case 2
assert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# Test case 3
assert spiral_order([[1]]) == [1]







def find_missing_number(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = 0
    actual_sum = 0
    
    for i in range(n + 1):
        expected_sum += i
    
    for num in nums:
        actual_sum += num
    
    return expected_sum - actual_sum

# Test case 1
assert find_missing_number([3, 0, 1]) == 2
# Test case 2
assert find_missing_number([0, 1]) == 2
# Test case 3
assert find_missing_number([9,6,4,2,3,5,7,0,1]) == 8

































def check_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

# Test cases
assert check_parentheses("()") == True
assert check_parentheses("()[]{}") == True
assert check_parentheses("(]") == False
assert check_parentheses("([)]") == False
assert check_parentheses("{[]}") == True