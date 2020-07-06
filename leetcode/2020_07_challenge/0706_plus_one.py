from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        ans = [0 for x in range(size)]
        carry = 1
        for n in range(size-1, -1, -1):
            #print(n, carry)
            plus = digits[n] + carry
            if plus > 9:
                ans[n] = 0
                carry = 1
            else:
                ans[n] = plus
                carry = 0
        if carry:
            ans.insert(0, carry)
        return ans

cases = [
    [1,2,3],
    [4,3,2,1],
    [9],
    [1,9],
    [2,9],
    [2,8],
    [9,9],
    [1,9,9],
    [9,9,9,9]
]

sol = Solution()
for case in cases:
    print(sol.plusOne(case))



        
