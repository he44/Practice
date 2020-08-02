from typing import *


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def case(char):
            return ord('A') <= ord(char) <= ord('Z')
        # except for the first char, all remaining should be same
        first = case(word[0])
        seen = None
        for char in word[1:]:
            cur = case(char)
            if seen is None:
                seen = cur 
            if seen != cur:
                return False
        if not first and seen:
            return False
        return True

cases = [
    'USA',
    'FlaG'
]

sol = Solution()

for case in cases:
    print(sol.detectCapitalUse(case))
                
