from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hmin = float('inf')
        hmax = 0
        wmin = float('inf')
        wmax = 0
        for hc in horizontalCuts:
            hmin = min(hmin, hc)
            hmax = max(hmax, hc)
        for wc in verticalCuts:
            wmin = min(wmin, wc)
            wmax = max(wmax, wc)
        hh = max(hmax - 0, h - hmin, hmax - hmin)
        ww = max(wmax - 0, w - wmin, wmax - wmin)
        print(hmax, hmin, wmax, wmin)
        print(hh, ww)
        return int((hh * ww) % (1e9+7))



s = Solution()
cases = [
    [5, 4, [1,2,4], [1,3]],
    [5, 4, [3,1], [1]],
    [5, 4, [3], [3]]
]

for h, w, hcs, vcs in cases:
    print(s.maxArea(h,w,hcs,vcs))

        
