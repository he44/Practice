from typing import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dps = [[1 for y in range(n)] for x in range(m)]
        for x in range(1, m):
            for y in range(1, n):
                dps[x][y] = dps[x-1][y] + dps[x][y-1]
        return dps[m-1][n-1]

cases = [
    (3, 2),
    (7, 3)
]

sol = Solution()
for m, n in cases:
    print(sol.uniquePaths(m,n))

