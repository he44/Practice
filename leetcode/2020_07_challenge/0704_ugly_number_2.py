from typing import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            new = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            nums.append(new)
            if new == nums[p2] * 2:
                p2 += 1
            if new == nums[p3] * 3:
                p3 += 1
            if new == nums[p5] * 5:
                p5 += 1
        return nums[-1]

cases = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

sol = Solution()

for case in cases:
    print(sol.nthUglyNumber(case))
