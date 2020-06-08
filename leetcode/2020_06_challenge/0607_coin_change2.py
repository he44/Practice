from typing import *

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for x in range(amount + 1)] for y in range(len(coins)+1)]
        #print(len(dp), len(dp[0]))
        dp[0][0] = 1
        for ci in range(len(coins)):
            coin = coins[ci]
            for val in range(amount + 1):
                dp[ci+1][val] = dp[ci][val]
                if coin <= val:
                    dp[ci+1][val] += dp[ci+1][val-coin]
        #print(dp)
        return dp[-1][-1]




cases = [
    [5, [1,2,5]],
    [3, [2]],
    [10, [10]]
]

s = Solution()
for amount, coins in cases:
    print(s.change(amount, coins))

