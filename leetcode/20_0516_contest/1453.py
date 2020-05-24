from typing import *

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        from math import sqrt
        nums = len(points)
        res = 1
        for i in range(nums):
            for j in range(i+1, nums):
                x1, y1 = points[i] 
                x2, y2 = points[j]
                d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d > 2 * r:
                    continue
                t = sqrt((r/d) ** 2 - 1/4)
                xc = ((x1 + x2)/2 - t * (y2-y1))
                yc = ((y1 + y2)/2 + t * (x2-x1))
                this_res = 2
                for k in range(nums):
                    if k == i or k == j:
                        continue
                    xk, yk = points[k]
                    if (xk-xc) ** 2 + (yk-yc) ** 2 <= r ** 2:
                        this_res += 1
                res = max(this_res, res)
        return res
                


def main():
    s = Solution()
    cases = [
        ([[-2,0],[2,0],[0,2],[0,-2]], 2),
        ([[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], 5),
        ([[-2,0],[2,0],[0,2],[0,-2]] ,1),
        ([[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], 2)
    ]
    for points, r in cases:
        print(s.numPoints(points, r))


if __name__ == "__main__":
    main()
        
