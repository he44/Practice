from typing import *

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        h = len(dungeon)
        if h == 0:
            return 0
        w = len(dungeon[0])

        # construct dp Need to keep in mind it has to be at least 1
        dps = [[float('inf') for y in range(w)] for x in range(h)]
        dps[h-1][w-1] = max(1, 1 - dungeon[h-1][w-1])
        for i in range(h-2, -1, -1):
            dps[i][w-1] = max(dps[i+1][w-1] - dungeon[i][w-1], 1)
        for j in range(w-2, -1, -1):
            dps[h-1][j] = max(dps[h-1][j+1] - dungeon[h-1][j], 1)
        # recursion
        for i in range(h-2, -1, -1):
            for j in range(w-2, -1, -1):
                # need to ensure it's positive
                # min(max(0, a), b) will give the smaller positive between a b
                dps[i][j] = min(dps[i+1][j], dps[i][j+1]) - dungeon[i][j]
                dps[i][j] = max(1, dps[i][j])
        #print(dps)
        return dps[0][0]

cases = [
    [[-2,-3,3],
     [-5, -10, 1],
     [10, 30, -5]
    ],
    [[100]],
    [[2,1],[1,-1]]
]

sol = Solution()
for case in cases:
    print(sol.calculateMinimumHP(case))


