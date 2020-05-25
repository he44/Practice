from typing import *

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        la = len(A)
        lb = len(B)
        print(la, lb)
        dp = [[0 for x in range(lb)] for y in range(la)]
        # dp part
        for x in range(la):
            for y in range(lb):
                if A[x] == B[y]:
                    if x-1 < 0 or y - 1 < 0:
                        dp[x][y] = 1
                    else:
                        dp[x][y] = dp[x-1][y-1] + 1
                else:
                    c1 = dp[x-1][y] if x-1 >= 0 else 0
                    c2 = dp[x][y-1] if y-1 >= 0 else 0
                    dp[x][y] = max(dp[x-1][y], dp[x][y-1])

        return dp[la-1][lb-1]


def main():
    s = Solution()        
    cases = [
        ([1,4,2], [1,2,4]),
        ([2,5,1,2,5], [10,5,2,1,5,2]),
        ([1,3,7,1,7,5], [1,9,2,5,1])
    ]
    for A, B in cases:
        print(s.maxUncrossedLines(A,B))

if __name__ == "__main__":
    main()

