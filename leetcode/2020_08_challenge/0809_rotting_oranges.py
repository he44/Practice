from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        rotten = set()
        fresh = set()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))
        # print(fresh)
        # print(rotten)
        timer = 0
        while fresh:
            # no  more newly rotten oranges to work with
            # print("fresh", fresh)
            # print("rotten", rotten)
            if not rotten:
                return -1
            # new rotten 
            new_rotten = set()
            for i, j in rotten:
                for di, dj in [(-1,0), (0, 1), (1, 0), (0, -1)]:
                    # need to use the fresh set to check, 
                    # we are not updating grid at all
                    #if 0 <= (i + di) < h and 0 <= (j + dj) < w and grid[i+di][j+dj] == 1:
                    if 0 <= (i + di) < h and 0 <= (j + dj) < w and (i+di,j+dj) in fresh:
                        new_rotten.add((i+di, j+dj))
            fresh -= new_rotten
            timer += 1
            rotten = new_rotten.copy()
        return timer

cases = [
    [[2,1,1],[1,1,0],[0,1,1]],
    [[2,1,1],[0,1,1],[1,0,1]],
    [[0,2]]
]

sol = Solution()
for case in cases[:]:
    print(sol.orangesRotting(case))


# BFS? shortest path from source to all?

# or just pure simulation?
# pure simulation takes O(n^3) at most? where n is the size of the grid
# at most n steps, at each step, iteratve over the entire grid

# m0
# [
    # [2,1,1],
    # [1,1,0],
    # [0,1,1]
# ]
# m1               
# [
    # [2,2,1],
    # [2,1,0],
    # [0,1,1]
# ]
# m2
# [
    # [2,2,2],
    # [2,2,0],
    # [0,1,1]
# ]
# m3
# [
    # [2,2,2],
    # [2,2,0],
    # [0,2,1]
# ]
# m4
# [
    # [2,2,2],
    # [2,2,0],
    # [0,2,2]
# ]
