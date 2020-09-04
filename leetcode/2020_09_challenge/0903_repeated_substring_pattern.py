from typing import *


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
                    

cases = [
    "abab",
    "aba",
    "abcabcabcabc"
]

sol = Solution()
for case in cases:
    print(sol.repeatedSubstringPattern(case))


