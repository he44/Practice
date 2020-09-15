from typing import *


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) == 0:
            return 0
        last_word = s.split()[-1]
        return len(last_word)


cases = [
    "Hello World",
    "",
    " "
]

sol = Solution()
for case in cases:
    print(sol.lengthOfLastWord(case))
        
