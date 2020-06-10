from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        # after insertion, next position
        #print(lo, hi)
        return lo if nums[lo] >= target else (lo + 1)

cases = [
    [[1], 1],
    [[1,3,5,6], 5],
    [[1,3,5,6], 2],
    [[1,3,5,6], 7],
    [[1,3,5,6], 0]
]

sol = Solution()
for nums, target in cases:
    print(sol.searchInsert(nums, target))
        
