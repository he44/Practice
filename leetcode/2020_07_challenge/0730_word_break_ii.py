from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def recursion(s):
            # empty string
            if not s:
                return [[]]
            # this substring is already solved?
            if s in memo:
                return memo[s]
            memo[s] = []
            for end in range(1, len(s)+1):
                candidate = s[:end]
                if candidate in wordDict:
                    breaking_the_rest = recursion(s[end:])
                    for rest in breaking_the_rest:
                        memo[s].append([candidate] + rest)
            return memo[s]

        memo = {}
        recursion(s)
        return [" ".join(words) for words in memo[s]]

#
# "cats" "and" "dog"
# 0 1 2 3 4 5 6 7 8 9
# c a t s a n d d o g
# prev_b = [0, 4, 7, 10]

cases = [
    ["catsanddog", ["cat", "cats", "and", "sand", "dog"]]
]
sol = Solution()
for s, wordDict in cases:
    print(sol.wordBreak(s, wordDict))