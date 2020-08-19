from typing import *


class Solution:
    # N: length of integers 
    # K: difference we need
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = []
        def dfs(depth, cur, partial_sol):
            # print(depth, cur, partial_sol)
            if depth == 0:
                ans.append(partial_sol)
                return 
            # case when K is 0
            neighbors = [-K, K] if K else [K]
            for i in neighbors:
                if 0 <= cur + i <= 9:
                    new_num = partial_sol * 10 + (cur + i)
                    dfs(depth - 1, cur + i, new_num)
        if N == 1:
            ans.append(0)
        for i in range(1, 10):
            dfs(N-1, i, i)
        return ans

cases = [
    (3, 7),
    (2, 1),
    (1, 0),
    (2, 0)
]

sol = Solution()
for case in cases:
    print(sol.numsSameConsecDiff(case[0], case[1]))



                    
