from typing import *

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # construct the intervals (meeting room scenario)
        intervals = []
        ps = {}
        prefix_sum = 0 
        n = len(nums)
        for i in range(-1, n):
            if i == -1:
                ps[prefix_sum] = [-1]
                continue
            prefix_sum += nums[i]

            if prefix_sum in ps:
                ps[prefix_sum].append(i)
            else:
                ps[prefix_sum] = [i]

            start_sum = prefix_sum - target
            if start_sum in ps:
                for start in ps[start_sum]:
                    if start + 1 <= i:
                        intervals.append((start + 1, i))
        

        # dp?
        # https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
        # okay greedy it is
        # sort all the subarrays by their finish index (no need, this interval is generated this way)?
        # intervals = sorted(intervals, key = lambda x: x[1])

        num_cands = len(intervals)
        if num_cands == 0:
            return 0
        count = 1
        earliest_start = intervals[0][1] + 1
        for k in range(1, num_cands):
            if intervals[k][0] >= earliest_start:
                count += 1
                earliest_start = intervals[k][1] + 1
        return count
                
        # TLE





cases = [
    [[1,1,1,1,1], 2],
    [[-1,3,5,1,4,2,-9], 6],
    [[-2,6,6,3,5,4,1,2,8], 10],
    [[0,0,0], 0]
]

sol = Solution()
for nums, target in cases:
    print(sol.maxNonOverlapping(nums, target))




                    

# Probably DP and backtracking?
# n = len(s)

# DP[k]: the maximum number of non-empty non-overlapping subarrays with target sum in s[...k+1]

# so essentially we want DP[n]

# recursion:
# DP[k] = max(DP[k-1]

# we can use the prefix sum to check?

# we probably need to track the last used index.. cause this defines the left most possible starting point?

# we have "zig-zag" the subarray somehow?

# s = [-1,3,5,1,4,2,-9], target = 6

# 1. prefix sum

    # ps = [-1, 2, 7, 8, 12, 14, 5]

    # we can find three possible subarrays by looking at the prefix sum

        # 1.) 8 - 2 = 6, start = 2, end = 3 (inclusive)
        # 2.) 14 - 8 = 6, start = 4, end = 5 (inclusive)
        # 3.) 5 - (-1) = 6, start = 1, end = 6 (inclusive)

# isn't this the same as the meeting scheduler problem?
