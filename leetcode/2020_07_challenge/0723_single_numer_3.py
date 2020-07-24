from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xy_diff = 0
        for num in nums:
            xy_diff = xy_diff ^ num

        # define a set bit (use the right most one)
        xy_diff = xy_diff & (-xy_diff)
        x = 0
        y = 0
        for num in nums:
            # this means that bit is not set
            if not num & xy_diff:
                x = x ^ num
            else:
                y = y ^ num

        return [x, y]


cases = [
    [1,2,1,3,2,5]
]

sol = Solution()
for case in cases:
    print(sol.singleNumber(case))
