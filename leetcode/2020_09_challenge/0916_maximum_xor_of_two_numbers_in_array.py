from typing import *


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(bin(max(nums))) - 2 # max number of bits
        max_xor = 0
        for i in range(n - 1, -1, -1):
            max_xor = max_xor << 1 # shift to the left, LSB to fill in 
            # try to have 1 in LSB
            hope = max_xor | 1
            prefixes = {num >> i for num in nums}
            for p in prefixes:
                if hope ^ p in prefixes:
                    max_xor = hope
                    break
        return max_xor


cases = [
    [3, 10, 5, 25, 2, 8]
]

sol = Solution()
for case in cases:
    print(sol.findMaximumXOR(case))




                    
