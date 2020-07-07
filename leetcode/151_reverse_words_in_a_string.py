from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        items = s.split()
        print(items)
        return ' '.join(items[::-1])

sol = Solution()

cases = [
    "the sky is blue",
    "  hello world!  ",
    "a good   example"
]

for case in cases:
    print(sol.reverseWords(case))