from typing import *

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == 'D':
                stack.append(i + 1)
            if s[i] == 'I':
                stack.append(i + 1)
                while stack:
                    res.append(stack.pop())
        res.append(len(s) + 1)
        while stack:
            res.append(stack.pop())
        return res




cases = [
    "I", "DI", "DDIIIID"
]

sol = Solution()
for case in cases:
    print(sol.findPermutation(case))
        
