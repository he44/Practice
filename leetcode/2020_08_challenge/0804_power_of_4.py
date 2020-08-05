from typing import *

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # power of 2, only one 1 in the binary representation
        # power of 4, only one 1 followed by even number of 0s
        # 2 10
        # 4 100 (y)
        # 8 1000
        # 16 10000 (y)
        # 32 1000000 (y)
        bin_pattern = bin(num)[2:]
        return (len(bin_pattern) % 2 == 1) and (bin_pattern[0] == '1') and (bin_pattern[1:] == "" or int(bin_pattern[1:]) == 0) 

cases = [
    0, 1, 2, 4, 5, 16
]

sol = Solution()
for case in cases:
    print(sol.isPowerOfFour(case))