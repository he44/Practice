from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def invalid_char(char):
            val = ord(char)
            return not(ord('a') <= val <= ord('z') or ord('0') <= val <= ord('9'))

        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            lc = s[lo].lower()
            hc = s[hi].lower()
            invalid_l = invalid_char(lc)
            invalid_h = invalid_char(hc)
            if not (invalid_l or invalid_h):
                if lc != hc:
                    return False
                lo += 1
                hi -= 1
            if invalid_l:
                lo += 1
            if invalid_h:
                hi -= 1
        return True


cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "0P"
]

sol = Solution()
for case in cases:
    print(sol.isPalindrome(case))
