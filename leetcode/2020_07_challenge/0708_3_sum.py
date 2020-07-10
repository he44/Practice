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

    def threeSum_from2sum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target):
            # since this is already sorted, we can do binary search?
            lo = 0
            hi = len(nums)-1
            res = []
            while lo < hi:
                tmp = nums[lo] + nums[hi]
                if tmp < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif tmp > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                # need to check duplicate first
                else:
                    res.append([-target, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return res

        # sort the list
        nums.sort()
        # go through each num
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                res += twoSum(nums[i+1:], -nums[i])
        return res

cases = [
    [-1, 0, 1, 2, -1, -4],
    [-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]
]

sol = Solution()
for case in cases:
    print(sol.threeSum_from2sum(case))


