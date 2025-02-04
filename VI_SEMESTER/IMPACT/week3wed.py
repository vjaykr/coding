from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        p = permutations(nums)
        g = list(p)

        res = ""
        for i in g[k-1]:
            res += i
        return res
    
n = 3
k = 3
print(Solution().getPermutation(n, k))  



#leet code problem number 65
import math
import re

def getPermutation(n: int, k: int) -> str:
    numbers = list(range(1, n + 1))
    k -= 1  # convert k to zero-based index
    permutation = []
    
    for i in range(n, 0, -1):
        factorial = math.factorial(i - 1)
        index = k // factorial
        permutation.append(str(numbers.pop(index)))
        k %= factorial
    
    return ''.join(permutation)

# Example usage:
n = 3
k = 3
print(getPermutation(n, k)) 


#leet code problem number 90
class Solution:
    def isNumber(self, s: str) -> bool:
        # Define a regular expression pattern for a valid number
        pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
        return bool(pattern.match(s))

# Example usage:
solution = Solution()
test_cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
results = [solution.isNumber(tc) for tc in test_cases]
print(results)


#or

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        
        # Flags to indicate if we have seen a digit, a dot, an exponent, and a sign
        seen_digit = seen_dot = seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                # Sign must be at the beginning or just after an exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char in ['e', 'E']:
                # Exponent must follow a digit and must not have been seen before
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Reset for the exponent part
            elif char == '.':
                # Dot must not have been seen before and must not be in the exponent part
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit

# Example usage:
solution = Solution()
test_cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
results = [solution.isNumber(tc) for tc in test_cases]
print(results)





#stack here

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Stack size:", stack.size())  # Output: Stack size: 3
    print("Top element:", stack.peek())  # Output: Top element: 3
    print("Popped element:", stack.pop())  # Output: Popped element: 3
    print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2
    
    
    
# queue here


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def size(self):
        return len(self.queue)

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue size:", q.size())  # Output: Queue size: 3
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 1
    print("Queue size:", q.size())  # Output: Queue size: 2
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 2
    print("Queue size:", q.size())  # Output: Queue size: 1
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 3
    print("Queue size:", q.size())  # Output: Queue size: 0    