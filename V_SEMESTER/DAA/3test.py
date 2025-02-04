class Solution(object):
    def gcd(self,a,b):
        while b:
            a,b = b,a%b
        return a
    
    def findGCD(self,nums):
        smallest = min(nums)
        largest = max(nums)
        return self.gcd(smallest,largest)
    
nums = [6,7,9] 
Solution = Solution()
result = Solution.findGCD(nums)
min = min(nums)
max = max(nums)
print(result)       
print(f'The greatest common divisor of {min} and {max} is {result} /n did you get it right?')