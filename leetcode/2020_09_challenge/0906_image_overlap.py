from typing import *

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def count(xs, ys, fixed, moved):
            overlap = 0
            for r in range(n - xs):
                for c in range(n - ys):
                    if fixed[xs + r][ys + c] == 1 and fixed[xs + r][ys + c] == moved[r][c]:
                        overlap += 1
            return overlap
        n = len(A)
        ans = 0
        x_shifts = [i for i in range(n)]
        y_shifts = [i for i in range(n)]
        for xs in x_shifts:
            for ys in y_shifts:
                ans = max(max, count(xs, ys, A, B))
                ans = max(max, count(xs, ys, B, A))
        return ans



