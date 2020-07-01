from typing import *

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        rows = 0
        while (n >= 0):
            n -= i
            rows += 1
            i += 1

        rows -= 1
        return rows

    def arrangeCoins_binary(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            #print(lo, mid, hi)
            num = mid * (mid + 1) // 2
            if num == n:
                return mid
            elif num < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi # hi is the smaller one now

    def arrangeCoins_math(self, n: int) -> int:
        # k(k+1)/2 <= n
        # k^2 + k - 2n <= 0
        # (k+1/2) ^ 2 - 1/4 <= 2n
        # (k + 1/2)^2 <= 2n + 1/4
        # (k+1/2) <= sqrt(2n + 1/4)
        # k <= sqrt(2n + 1/4) - 1/2 floor function
        return int((2 * n + 1/4)**0.5-0.5)


cases = [1,2,3,4,5,6,7,8,9,10]
#cases = [9]

sol = Solution()
for case in cases:
    print(case, sol.arrangeCoins_math(case), sol.arrangeCoins_binary(case), sol.arrangeCoins(case))
