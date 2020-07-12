from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(2 ** n, 2 ** (n+1)):
            pattern = bin(i)[3:]
            print(pattern)
            subset = [nums[j] for j in range(n) if pattern[j] == "1"]
            res.append(subset)
        return res
            
cases = [
    [1,2,3]
]

sol = Solution()
for case in cases:
    print(sol.subsets(case))
