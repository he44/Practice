from typing import *


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        newqueue = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for h,k in people:
            newqueue.insert(k, (h,k))
        return newqueue



cases = [
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
]

s = Solution()

for case in cases:
    print(s.reconstructQueue(case))
