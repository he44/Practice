from typing import *


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


cases = [
    38
]

sol = Solution()
for case in cases:
    print(sol.addDigits(case))
