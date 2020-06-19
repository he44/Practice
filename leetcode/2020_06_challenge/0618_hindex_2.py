from typing import *

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if citations[mid] == (n - mid):
                print("here", lo, hi, mid)
                return (n-mid)
            elif citations[mid] < (n-mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return n-lo


cases = [
    [0]
]

sol = Solution()

for case in cases:
    print(sol.hIndex(case))

