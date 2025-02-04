class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)
        return self.gcd(smallest, largest)

nums = [2, 5, 6, 9, 10]
solution = Solution()
result = solution.findGCD(nums)
print(result)