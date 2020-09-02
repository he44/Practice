from typing import *

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1
        import itertools
        for h,i,j,k in itertools.permutations(A):
            hour = 10 * h + i
            minute = 10 * j + k
            if hour <= 23 and minute <= 59:
                max_time = max(max_time, hour * 60 + minute)
        if max_time == -1:
            return ""
        return ("%02d:%02d")%(max_time // 60, max_time % 60)



cases = [
    # [1,2,3,4],
    # [5,5,5,5],
    # [1,1,1,1],
    # [1,1,1,2],
    # [1,9,6,0],
    [2,0,6,6]
]

sol = Solution()
for case in cases:
    print(sol.largestTimeFromDigits(case))

                    
