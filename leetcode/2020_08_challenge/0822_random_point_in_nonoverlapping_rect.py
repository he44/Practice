from typing import *


class Solution:

    def __init__(self, rects: List[List[int]]):
        # simulate the cdf first
        self.n = len(rects)
        self.rects = rects
        self.cdf = [0 for _ in range(self.n)]
        # including the perimeter
        self.cdf[0] = (rects[0][3] - rects[0][1] + 1) * (rects[0][2] - rects[0][0] + 1)
        for i in range(1, self.n):
            self.cdf[i] = self.cdf[i-1] + (rects[i][3] - rects[i][1] + 1) * (rects[i][2] - rects[i][0] + 1)
        self.total = self.cdf[-1]

    def pick(self) -> List[int]:
        import random
        target = random.randint(0, self.total)
        lo = 0
        hi = self.n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target >= self.cdf[mid]:
                lo = mid + 1
            else:
                hi = mid
        pts_x = random.randint(self.rects[lo][0], self.rects[lo][2])
        pts_y = random.randint(self.rects[lo][1], self.rects[lo][3])
        return [pts_x, pts_y]


    def __repr__(self):
        return ("CDF: " + str(self.cdf) + '\n' + "Total: " + str(self.total) )


cases = [
    [[1,1,5,5]],
    [[-2,-2,-1,-1],[1,0,3,0]]
]

for case in cases:
    sol = Solution(case)
    print(sol)
    print(sol.pick())
