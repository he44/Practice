from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = {}
        # O(n) to get frequency
        for num in nums:
            if num not in counters:
                counters[num] = 1
            else:
                counters[num] += 1
        # print(counters)
        import heapq
        return heapq.nlargest(k, [key for key in counters], key=lambda x: counters[x])

cases = [
    [[1,1,1,2,2,3], 2],
    [[1], 2]
]

sol = Solution()

for nums, k in cases:
    print(sol.topKFrequent(nums, k))