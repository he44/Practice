from typing import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            dists.append(dist)
        # sort two lists by the first one
        sdists, spts = zip(*sorted(zip(dists, points)))
        return list(spts)[:K]

        

def main():
    s = Solution()
    cases = [
        [[[1,3], [-2,2]], 1],
        [[[3,3],[5,-1],[-2,4]], 2]
    ]
    for pts, k in cases:
        print(s.kClosest(pts, k))

if __name__ == "__main__":
    main()
