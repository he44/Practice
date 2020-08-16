from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on starting point
        intervals.sort(key = lambda x:x[1])
        # greedy
        prev_end = float('-inf')
        count = 0
        for start, end in intervals:
            if start >= prev_end:
                # pick
                prev_end = end
            else:
                # remove
                count += 1
        return count






cases = [
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[1,2],[2,3]]
]

sol = Solution()
for case in cases:
    print(sol.eraseOverlapIntervals(case))
