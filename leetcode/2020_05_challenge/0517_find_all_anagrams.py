from typing import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        window = [0 for x in range(26)]
        target = [0 for x in range(26)]
        for char in p:
            target[ord(char) - ord('a')] += 1
        tlen = len(p)
        res = []
        # build first window
        for i in range(tlen):
            window[ord(s[i]) - ord('a')] += 1
        # move window
        for i in range(tlen, len(s)):
            # check current window
            if window == target:
                res.append(i - tlen)
            # update current window
            window[ord(s[i- tlen]) - ord('a')] -= 1
            window[ord(s[i]) - ord('a')] += 1
        # check at last position
        if window == target:
            res.append(len(s) - tlen)
        return res


def main():
    sol = Solution() 
    testcases = [
        ('cbaebabacd', 'abc'),
        ('abab', 'ab')
    ]
    for s,p in testcases:
        print(sol.findAnagrams(s,p))

if __name__ == "__main__":
    main()
        
