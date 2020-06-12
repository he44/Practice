from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        p0 = 0
        p2 = len(nums) - 1
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1



cases = [
    [2,0,2,1,1,0]
]

sol = Solution()
for case in cases:
    print("Before", case)
    sol.sortColors(case)
    print("After", case)
        
