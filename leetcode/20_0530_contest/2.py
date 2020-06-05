from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        hmax = max(horizontalCuts[0], h - horizontalCuts[-1])
        wmax = max(verticalCuts[0], w - verticalCuts[-1])
        for hi in range(1, len(horizontalCuts)):
            hmax = max(hmax, horizontalCuts[hi] - horizontalCuts[hi-1])
        for wi in range(1, len(verticalCuts)):
            wmax = max(wmax, verticalCuts[wi] - verticalCuts[wi-1])
        return int((hmax * wmax) % (1e9+7))



s = Solution()
cases = [
    [5, 4, [1,2,4], [1,3]],
    [5, 4, [3,1], [1]],
    [5, 4, [3], [3]],
    [5, 2, [3,1,2], [1]]
]

for h, w, hcs, vcs in cases:
    print(s.maxArea(h,w,hcs,vcs))

        
