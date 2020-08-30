from typing import *
 
# 1 <= A.length <= 100
# 1 <= A[i] <= A.length

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def pancakeFlip(k, A):
            i = 0
            while i <= k // 2:
                A[i], A[k-i] = A[k-i], A[i]
                i += 1

        n = len(A)
        ans = []
        for i in range(n, 0, -1):
            old_idx = A.index(i)
            new_idx = i - 1
            if old_idx != new_idx:
                # only flip to head if it's not originally at head
                if old_idx != 0:
                    pancakeFlip(old_idx, A)
                    ans.append(old_idx + 1)
                pancakeFlip(new_idx, A)
                ans.append(new_idx + 1)
        return ans


cases = [
    [3,2,4,1],
    [1,2,3]
]

sol = Solution()
for case in cases:
    print(sol.pancakeSort(case))

        
