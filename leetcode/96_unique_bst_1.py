from typing import *
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        for k in range(3, n+1):
            numk = 0
            for i in range(k):
                numk += dp[i] * dp[k-1-i]
                #print(k, i, dp[i] * dp[k-1-i])
            dp.append(numk)
        return dp[n]





def main():
    s = Solution()
    cases = [1, 2, 3, 4, 5, 6]
    for n in cases:
        print(s.numTrees(n))

if __name__ == "__main__":
    main()




