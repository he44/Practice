from typing import *

class Solution:
    def makeGood(self, s: str) -> str:
        list_s = [char for char in s]
        good_string = False
        while not good_string:
            good_string = True
            n = len(list_s)
            for i in range(n-1):
                if list_s[i] != list_s[i+1] and list_s[i].lower() == list_s[i+1].lower():
                    good_string = False
                    list_s.pop(i)
                    list_s.pop(i) # after popping i, i + 1 became the new i
                    break
        return ''.join(list_s)


                

cases = [
    "leEeetcode",
    "abBAcC",
    "s"
]

sol = Solution()
for case in cases:
    print(sol.makeGood(case))

