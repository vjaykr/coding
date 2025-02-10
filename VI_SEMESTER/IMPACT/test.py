class Solution:
    def findClosestElements(self, arr, k, x):
        lo = 0
        hi = len(arr) - 1
        while hi - lo >= k:
            if abs(arr[lo] - x) > abs(arr[hi] - x):
                lo += 1
            else:
                hi -= 1
        result = []
        for i in range(lo, hi + 1):
            result.append(arr[i])
        return result
