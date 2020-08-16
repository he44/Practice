from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left_profits = [0 for x in range(len(prices))]
        right_profits = [0 for x in range(len(prices) + 1)]
        left_min = prices[0]# always buy here
        right_max = prices[-1] # always sell here
        for i in range(len(prices)):
            left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

            ri = len(prices) - i - 1
            right_profits[ri] = max(right_profits[ri+1], right_max - prices[ri])
            right_max = max(right_max, prices[ri])
        
        mp = 0
        for i in range(len(prices)):
            mp = max(mp, left_profits[i] + right_profits[i+1])
        return mp


cases = [
    [3,3,5,0,0,3,1,4],
    [1,2,3,4,5],
    [7,6,4,3,1]
]

sol = Solution()
for case in cases:
    print(sol.maxProfit(case))
