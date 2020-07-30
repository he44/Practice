from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = float('-inf')
        sold = float('-inf')
        reset = 0
        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price) #either nothing, or buy
            reset = max(pre_sold, reset) # either sold yesterday and wiathing, or nothing
        return max(sold, held, reset)

cases = [
    [1, 2, 3, 0, 2]
]

sol = Solution()

for case in cases:
    print(sol.maxProfit(case))
