from typing import *

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            # might be better to put this in else, but won't matter for this problem
            nums[abs(num) - 1 ] *= -1
        return ans

cases = [
    [4,3,2,7,8,2,3,1]
]

sol = Solution()

for case in cases:
    print(sol.findDuplicates(case))

# Example:
# [4, 3, 2, 7, 8, 2, 3, 1]
# [4, 3, 2, -7, 8, 2, 3, 1]
# [4, 3, -2, -7, 8, 2, 3, 1]
# [4, -3, -2, -7, 8, 2, 3, 1]
# [4, -3, -2, -7, 8, 2, -3, 1]
# [4, -3, -2, -7, 8, 2, -3, -1]
# [4, -3, -2, -7, 8, 2, -3, -1], ans = [2]
# [4, -3, -2, -7, 8, 2, -3, -1], ans = [2, 3]
# [-4, -3, -2, -7, 8, 2, -3, -1], ans = [2, 3]


