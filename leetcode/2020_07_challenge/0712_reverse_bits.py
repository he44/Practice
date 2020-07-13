from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_pattern = bin(n)[2:]
        print(bin_pattern)
        for bit in bin_pattern[::-1]:
            print(bit)



cases = [
    12,
    13
]


sol = Solution()
for case in cases:
    print(sol.reverseBits(case))


