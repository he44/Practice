from typing import *


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR two numbers and find number of 1s
        diff = x ^ y
        dist = 0
        while diff:
            if diff & 1:
                dist += 1
            diff = diff >> 1
        return dist

cases = [
    (1,4), (2,4)
]

sol = Solution()
for x, y in cases:
    print(sol.hammingDistance(x,y))