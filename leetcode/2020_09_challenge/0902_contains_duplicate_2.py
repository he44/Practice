from typing import *

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # t is bucket size (value difference)
        # i, j must differ by at most k
        if t < 0:
            return False
        n = len(nums)
        d = {}
        w = t + 1 # bucket width
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m+1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i-k] // w]
        return False


cases = [
    [[1,2,3,1], 3, 0],
    [[1,0,1,1], 1, 2],
    [[1,5,9,1,5,9], 2, 3]
]

sol = Solution()

for case, k, t in cases:
    print(sol.containsNearbyAlmostDuplicate(case, k, t))
