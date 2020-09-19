from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

cases = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]

sol = Solution()
for case in cases:
    print(sol.maxProfit(case))


        
