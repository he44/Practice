from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0 or m == 0:
            return n + m
        # adding sentinel array
        dps = [[0 for x in range(m + 1)] for y in range(n + 1)]

        # [0][0] represents two empty strings
        # 1st row/col used to denote if one string is empty
        for i in range(n + 1):
            dps[i][0] = i
        for j in range(m + 1):
            dps[0][j] = j

        # fill in the first row and columns

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    dps[i][j] = dps[i-1][j-1]
                else:
                    dps[i][j] = min(dps[i-1][j], dps[i][j-1], dps[i-1][j-1]) + 1
        return dps[n][m]


s = Solution()

cases = [
    ("sea", "eat")
]
        
for w1, w2 in cases:
    print(s.minDistance(w1, w2))

