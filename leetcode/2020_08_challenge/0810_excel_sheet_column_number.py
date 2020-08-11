from typing import *

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        mul = 1
        for char in s[::-1]:
            res += mul * (ord(char) - ord('A') + 1)
            mul *= 26
        return res

cases = [
    "A",
    "AB",
    "ZY",
    ""
]

sol = Solution()
for case in cases:
    print(sol.titleToNumber(case))




# A 1
# B 2



# Z 26
# AA 27
# AB 28

# ZY

# Y: 25
# Z: 26 * 26 = 676
# 676 + 25 = 701
                    
