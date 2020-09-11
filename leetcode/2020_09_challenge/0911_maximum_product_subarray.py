from typing import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_so_far = nums[0] # positive
        min_so_far = nums[0] # negative
        ans = max_so_far
        for i in range(1, n):
            num = nums[i]
            candidates = [num, max_so_far * num, min_so_far * num]
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            ans = max(max_so_far, ans)
        return ans


        
        
cases = [
    [1,0,-1,2,3,-5,-2]
# [1,2,3,4]
]

sol = Solution()
for case in cases:
    print(sol.maxProduct(case))
