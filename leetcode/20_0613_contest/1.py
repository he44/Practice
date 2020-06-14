from typing import *


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        rs = [nums[0]]
        for i in range(1,n):
            rs.append(rs[-1] + nums[i])
        return rs

        



cases = [
    [1,2,3,4],
    [1,1,1,1,1],
    [3,1,2,10,1],
    []
]
sol = Solution()

for case in cases:
    print(sol.runningSum(case))
