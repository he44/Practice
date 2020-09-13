from typing import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(interval1, interval2):
            min_end = min(interval1[1], interval2[1])
            max_start = max(interval1[0], interval2[0])
            return min_end >= max_start
        
        n = len(intervals)
        if n == 0:
            return [newInterval]
        m_s = n 
        m_e = -1 
        for i in range(n):
            interval = intervals[i]
            if overlap(interval, newInterval):
                m_s = min(i, m_s)
                m_e = max(i, m_e)
        # no merging
        if m_s == n and m_e == -1:
            flag = False
            for i in range(n-1):
                if intervals[i][0] < newInterval[0] and intervals[i+1][0] > newInterval[1]:
                    flag = True
                    break
            res = intervals[:]
            print(flag)
            if flag:
                pos = i + 1
            else:
                pos = n if intervals[0][0] < newInterval[0] else 0
            res.insert(pos, newInterval)
            return res
        print("ms me", m_s, m_e)
        merged_interval = [min(intervals[m_s][0], newInterval[0]), max(intervals[m_e][1], newInterval[1])]
        res = []
        i = 0
        while i < n:
            if m_s <= i <= m_e:
                res.append(merged_interval)
                i = m_e
            else:
                res.append(intervals[i])
            i += 1
        return res






cases = [
    [[[1,3],[6,9]], [2,5]],
    [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]],
    [[[1,5]], [6,8]],
    [[[3,5],[12,15]], [6,6]],
    [[[1,5]],[0,0]],
]
        
sol = Solution()
for intervals, newInterval in cases:
    print(sol.insert(intervals, newInterval))
