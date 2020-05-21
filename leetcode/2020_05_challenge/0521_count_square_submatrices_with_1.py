from typing import *

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        #  largest possible square
        k = min(m,n)

        res = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    continue
                # first row/col, no preceding cells
                if r == 0 or c == 0:
                    res += 1 # one size 1 square
                else:
                    matrix[r][c] = min(matrix[r-1][c], matrix[r-1][c-1], matrix[r][c-1]) + 1
                    res += matrix[r][c]
        return res

        
