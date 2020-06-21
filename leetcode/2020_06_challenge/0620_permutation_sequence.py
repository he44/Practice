from typing import *

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [x for x in range(1, n+1)]
        rk = k - 1 # make the math work, 0-index everything
        # factorial table, O(n) to compute, table[i] is i!
        fac_table = [1 for x in range(n+1)]
        for n in range(1, n + 1):
            fac_table[n] = fac_table[n-1] * n
        # recursion
        res = []
        while rk > 0:
            idx = rk // fac_table[n-1]
            res.append(nums.pop(idx))
            rk -= idx * fac_table[n-1]
            n -= 1
            #print(idx, res, rk)
        res += nums
        return ''.join([str(x) for x in res])
        

cases = [
    (3, 3),
    (4, 9),
    (4, 20)
]

sol = Solution()

for case in cases:
    print(sol.getPermutation(case[0], case[1]))
