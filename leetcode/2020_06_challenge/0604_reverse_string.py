from typing import *

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        fp = 0
        sp = n-1
        while fp < sp:
            s[fp], s[sp] = s[sp], s[fp]
            fp += 1
            sp -= 1
        

cases = [
    ["h","e","l","l","o"],
    ["H","a","n","n","a","h"]
]

s = Solution()

for case in cases:
    print("Before: ", case)
    print(s.reverseString(case))
    print("After: ", case)
