from typing import *

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        last = n - 1
        i = 0
        while i < last:
            # odd
            if A[i] % 2:
                A[i], A[last] = A[last], A[i]
                last -= 1
                i -= 1
            i += 1
        return A



cases = [
    [3,1,2,4],
    [1,2,3,4,5],
    [1],
    []
]
                    
sol = Solution()
for case in cases:
    print(case)
    print(sol.sortArrayByParity(case))
