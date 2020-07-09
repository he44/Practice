from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sum2_dict = {}
        for i in range(n):
            for j in range(i+1, n):
                need = -(nums[i] + nums[j])
                pair = (i, j) # keep the index, not the number; already sorted
                if need in sum2_dict:
                    sum2_dict[need].append(pair)
                else:
                    sum2_dict[need] = [pair]

        res = {}
        for i in range(n):
            z = nums[i]
            if z in sum2_dict:
                for x, y in sum2_dict[z]:
                    if i == x or i == y:
                        continue
                    trip = []
                    rx = min(nums[x], nums[y])
                    ry = max(nums[x], nums[y])
                    if z < rx:
                        trip = (z, rx, ry)
                    elif z > ry:
                        trip = (rx, ry, z)
                    else:
                        trip = (rx, z, ry)
                    if trip not in res:
                        res[trip] = 1
        return [[x[0], x[1], x[2]] for x in res]





cases = [
    [-1, 0, 1, 2, -1, -4]
]

sol = Solution()
for case in cases:
    print(sol.threeSum(case))


