from typing import *

"""
This is O(n) extra space?
"""
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen:
                return num
            seen[num] = 1
"""

"""
Try using Linked List
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        return fast


cases = [
    [1,3,4,2,2],
    [3,1,3,4,2]
]

sol = Solution()
for case in cases:
    print(sol.findDuplicate(case))
