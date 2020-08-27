from typing import *

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binary_search(i, intervals):
            small = intervals[i][1]
            lo = i + 1
            hi = len(intervals) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if intervals[mid][0] < small:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        interval_to_idx = {}
        for i in range(len(intervals)):
            # list cannot be dict keys in python
            interval_to_idx[tuple(intervals[i])] = i

        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        ans = [0 for _ in range(len(intervals))]
        for i in range(len(intervals)):
            ti = binary_search(i, sorted_intervals)
            if 0 <= ti < len(intervals):
                ai = interval_to_idx[tuple(sorted_intervals[ti])]
            else:
                ai = -1
            ans[interval_to_idx[tuple(sorted_intervals[i])]] = ai
        return ans


cases = [
    [[1,2]],
    [[3,4],[2,3],[1,2]],
    [[1,4],[2,3],[3,4]],
    []
]

sol = Solution()
for case in cases:
    print(case)
    print(sol.findRightInterval(case))
