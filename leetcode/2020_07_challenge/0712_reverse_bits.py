from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        bin_pattern = bin(n)[2:]
        print(bin_pattern)
        res = 0
        i = 32 - len(bin_pattern)
        for bit in bin_pattern:
            if bit == "1":
                res += (2 ** i)
            i += 1
        return res



cases = [
    43261596
]


sol = Solution()
for case in cases:
    print(sol.reverseBits(case))


