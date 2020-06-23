from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = 0
        seen_twice = 0 
        for num in nums:
            seen_once = (~seen_twice) & (seen_once ^ num)
            seen_twice = (~seen_once) & (seen_twice ^ num)
        return seen_once

cases = [
    [2,2,3,2],
    [0,1,0,1,0,1,99]
]

sol = Solution()
for case in cases:
    print(sol.singleNumber(case))
        
