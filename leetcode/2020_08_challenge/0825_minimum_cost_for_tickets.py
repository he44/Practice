from typing import *

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # travel days
        tdays = set(days)
        # dp[i]: min cost to pay for traverl days[:i]
        # 0 is a sentinel node
        dp = [0 for _ in range(366)]

        # recursion
        for i in range(366):
            if (i) not in tdays:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                            dp[max(0, i-1)] + costs[0], 
                            dp[max(0,i-7)] + costs[1], 
                            dp[max(0, i-30)] + costs[2]
                        )
        # print(dp)
        return dp[365]


cases = [
    [[1,4,6,7,8,20], [2,7,15]],
    [[1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]],
    [[1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50]],
    [[1,4,6,7,8,365], [2,7,15]]
]

sol = Solution()
for days, costs in cases:
    print(sol.mincostTickets(days, costs))
                    
