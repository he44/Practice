from typing import *

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        res = n
        rem = 0
        while res > 1:
            rem = res % 2
            res /= 2
            if rem:
                return False
        return True


cases = [
    1, 
    16, 
    218,
    0,
    -16
]
        
sol = Solution()
for case in cases:
    print(sol.isPowerOfTwo(case))
