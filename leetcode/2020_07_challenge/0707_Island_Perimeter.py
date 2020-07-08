from typing import *


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        neighbor_rcs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        perimeter = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] != 0:
                    shared = 0
                    for ri, ci in neighbor_rcs:
                        rn = r + ri
                        cn = c + ci
                        # thanks to Pycharm, I now know Python supports chained comparison
                        if h > rn >= 0 and w > cn >= 0:
                            if grid[rn][cn] == 1:
                                shared += 1
                    perimeter += (4 - shared)

        return perimeter

    def islandPerimeter_slightlybetter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        neighbor_rcs = [(-1, 0), (0, -1)]
        perimeter = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] != 0:
                    perimeter += 4
                    for ri, ci in neighbor_rcs:
                        rn = r + ri
                        cn = c + ci
                        # top/left only, 1 side needs checking
                        if rn >= 0 and cn >= 0:
                            if grid[rn][cn] == 1:
                                perimeter -= 2

        return perimeter


cases = [
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]
]

sol = Solution()
for case in cases:
    print(sol.islandPerimeter_slightlybetter(case))
