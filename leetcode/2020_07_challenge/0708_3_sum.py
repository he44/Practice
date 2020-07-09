from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        found = set()
        dups = set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 in dups:
                continue
            dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -(val1 + val2)
                if complement in seen and seen[complement] == i:
                    rmin = min(val1, val2, complement)
                    rmax = max(val1, val2, complement)
                    if (rmin, rmax) not in found:
                            found.add((rmin, rmax))
                            res.append([val1, val2, complement])
                seen[val2] = i
        return res


cases = [
    [-1, 0, 1, 2, -1, -4]
]

sol = Solution()
for case in cases:
    print(sol.threeSum(case))


