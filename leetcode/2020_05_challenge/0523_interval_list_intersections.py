from typing import *

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aidx = 0
        bidx = 0
        res = []
        while aidx < len(A) and bidx < len(B):
            ast, aed = A[aidx]
            bst, bed = B[bidx]
            if aed < bst:
                aidx += 1
            elif bed < ast:
                bidx += 1
            else:
                rs = max(ast, bst)
                re = min(aed, bed)
                res.append([rs, re])
                if re == aed:
                    aidx += 1
                if re == bed:
                    bidx += 1
        return res



def main():
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    s = Solution()
    print(s.intervalIntersection(A,B))


if __name__ == "__main__":
    main()
        
