from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [0 for _ in range(n+1)]
        for i in range(n):
            DP[i+1] = max(DP[i-1] + nums[i], DP[i])
        return DP[n]

cases = [
    [1,2,3,1],
    [2,7,9,3,1],
    []
]

sol = Solution()
for case in cases:
    print(sol.rob(case))
