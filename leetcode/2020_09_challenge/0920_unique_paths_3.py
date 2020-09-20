from typing import *

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # grab info
        row, col = len(grid), len(grid[0])
        start_r = 0
        start_c = 0
        empty_count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] >= 0:
                    empty_count += 1
                if grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def backtrack(r, c, empty_count):
            # base case: reached destination
            if grid[r][c] == 2 and empty_count == 1:
                return 1
            
            # recursion
            # marking current as visited
            tmp = grid[r][c]
            grid[r][c] = -2
            res = 0
            for ri, ci in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rn = r + ri
                cn = c + ci
                # out of bound
                if not (0 <= rn < row and 0 <= cn < col):
                    continue
                # obstacle cell or visited cell
                if grid[rn][cn] < 0:
                    continue
                res += backtrack(rn, cn, empty_count - 1)
            grid[r][c] = tmp
            return res
        
        return backtrack(start_r, start_c, empty_count)
        
