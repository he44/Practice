from typing import *


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        sn_1 = 2
        sn_2 = 1
        for k in range(3, n+1):
            sn = sn_1 + sn_2
            sn_2 = sn_1
            sn_1 = sn
        return sn

cases = range(1, 11)
sol = Solution()
for case in cases:
    print(sol.climbStairs(case))