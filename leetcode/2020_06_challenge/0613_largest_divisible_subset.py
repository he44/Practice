from typing import *

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        # sort the numbers
        nums.sort()
        # dp
        dps = [[nums[x]] for x in range(n)]
        for cur in range(n):
            append = []
            max_to_append = 0
            for i in range(cur-1, -1, -1):
                if nums[cur] % nums[i] == 0 and len(dps[i]) > max_to_append:
                    max_to_append = len(dps[i])
                    append = dps[i]
            dps[cur] = append + dps[cur]
        # find the largest
        dps.sort(key = lambda x: len(x))
        return dps[-1]


cases = [
    [1,2,3],
    [1,2,4,8],
    [],
    [4, 8, 10, 240]
]

sol = Solution()
for case in cases:
    print(sol.largestDivisibleSubset(case))
