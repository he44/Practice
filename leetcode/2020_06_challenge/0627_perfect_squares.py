from typing import *

class Solution:
    def numSquares(self, n: int) -> int:
        import math
        max_sroot = int(math.sqrt(n))
        # all the square numbers available
        squares = [i ** 2 for i in range(1, max_sroot+1)]
        dps = [float('inf') for x in range(n + 1)]
        dps[0] = 0
        # construct the dps array
        for i in range(1+n):
            for square in squares:
                if square <= i:
                    dps[i] = min(dps[i], dps[i-square] + 1)


        return dps[n]

    def numSquares_greedy(self, n: int) -> int:
        import math
        def is_divided_by(n, count):
            # base case
            if count == 1:
                return (n == (int(math.sqrt(n)))**2)
            # recursion
            for square in squares:

                if square < n and is_divided_by(n-square, count-1):
                    return True
            return False

        max_sroot = int(math.sqrt(n))
        squares = [i ** 2 for i in range(1, max_sroot+1)]
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count


cases = [
    7, 12, 13
]

sol = Solution()
for case in cases:
    print(sol.numSquares_greedy(case))
