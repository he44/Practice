from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            half = helper(x,n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        return helper(x, n) if n >= 0 else helper(1/x,-n)

cases = [
    (2, 10),
    (2.1, 3),
    (2, -2)
]

sol = Solution()
for x, n in cases:
    print(sol.myPow(x,n))