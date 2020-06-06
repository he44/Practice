from typing import *

import random

class Solution:

    def __init__(self, w: List[int]):
        self.psm = []
        prefix = 0
        for weight in w:
            prefix += weight
            self.psm.append(prefix)
        self.tw = prefix
        print("psum length", len(self.psm))
        print(self.psm, self.tw)
        

    def pickIndex(self) -> int:
        tp = random.random() * self.tw
        lo = 0
        hi = len(self.psm) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            # target index
            if tp > self.psm[mid]:
                lo = mid + 1
            else:
                hi = mid
            #print(lo, hi)
        print("target is ", tp, "returned ", lo)
        return lo

    def test(self, tp) -> int:
        lo = 0
        hi = len(self.psm) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            # target index
            if tp > self.psm[mid]:
                lo = mid + 1
            else:
                hi = mid
            #print(lo, hi)
        print("target is ", tp, "returned ", lo)
        return lo

        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

cases = [
    [3, 14, 1, 7]
]

for case in cases:
    print("Case:", case)
    s = Solution(case)
    print(s.test(5))
    """
    for i in range(10):
        print(s.pickIndex())
    """
