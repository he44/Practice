from typing import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        dps = [[False for x in range(lt + 1)] for y in range(ls + 1)]
        # t is empty
        for i in range(ls + 1):
            dps[i][lt] = False
        # s is empty
        for i in range(lt + 1):
            dps[ls][i] = True
        # recursion
        for si in range(ls-1, -1, -1):
            for ti in range(lt-1, -1, -1):
                dps[si][ti] = ((s[si] == t[ti]) and dps[si+1][ti+1]) or (dps[si][ti+1])
        return dps[0][0]




cases = [
    ["abc", "ahbgdc"],
    ["axc", "ahbgdc"]
]


sol = Solution()
for s,t in cases:
    print(sol.isSubsequence(s, t))

        
