from typing import *

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        if N == 0:
            return 0
        # counting sort (actually saw this from geohot video before...)
        # replace all ciations larger than N to be N
        count = [0 for _ in range(N + 1)]
        for i in range(N):
            if citations[i] > N:
                citations[i] = N
            count[citations[i]] += 1
        k = N
        s = count[-1]
        while s < k:
            k -= 1
            s += count[k]
        return k
            



cases = [
    [3,0,6,1,5],
    [],
    [1]
]

sol = Solution()

for case in cases:
    print(sol.hIndex(case))
                    
