from typing import *

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(target, cur, start):
            # print(cur)
            # solution found
            if target == 0 and len(cur) == k:
                ans.append(cur[:])
                return
            # no solution possible
            elif target < 0 or len(cur) == k:
                return
            for i in range(start + 1, 10):
                cur.append(i)
                backtrack(target - i, cur, i)
                cur.pop()


        ans = []
        backtrack(n, [], 0)
        return ans

                    
cases = [
    [3, 7],
    [3, 9]
]

sol = Solution()
for k,n in cases:
    print(sol.combinationSum3(k, n))
