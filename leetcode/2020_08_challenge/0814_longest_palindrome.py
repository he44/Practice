from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        for char in s:
            if char in seen:
                seen.remove(char)
            else:
                seen.add(char)
        return len(s) - max((len(seen) - 1), 0)
                    
cases = [
    "abccccdd",
    "",
    "bb",
    "abcdedf"
]
sol = Solution()
for case in cases:
    print(sol.longestPalindrome(case))
