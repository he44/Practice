from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[lo] > nums[mid]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        return nums[lo]


cases = [
    [1, 3, 5],
    [2, 2, 2, 0, 1]
]

sol = Solution()

for case in cases:
    print(sol.findMin(case))