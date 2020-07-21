from typing import *

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        flag = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        dividend = dividend if dividend > 0 else - dividend
        divisor = divisor if divisor > 0 else - divisor
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return quotient if not flag else -quotient

cases = [
    (10, 3),
    (7, -3),
    (0, 3),
    (0, -3),
    (-9, -3),
    (-9, 3)
]

sol = Solution()
for dividend, divisor in cases:
    print(sol.divide(dividend, divisor))