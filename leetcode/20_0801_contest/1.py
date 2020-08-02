from typing import *
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def check(i, j, k, a, b, c):
            r1 = abs(i-j) <= a
            r2 = abs(j-k) <= b
            r3 = abs(i-k) <= c
            return (r1 and r2 and r3)
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if check(arr[i], arr[j], arr[k], a, b, c):
                        res += 1
        return res