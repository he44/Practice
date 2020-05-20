from typing import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        window = {}
        target = {}
        for i in range(l1):
            if s1[i] not in target:
                target[s1[i]] = 1
            else:
                target[s1[i]] += 1

            if s2[i] not in window:
                window[s2[i]] = 1
            else:
                window[s2[i]] += 1

        if window == target:
            return True

        for i in range(l1, l2):
            # update the window
            if s2[i] not in window:
                window[s2[i]] = 1
            else:
                window[s2[i]] += 1
            window[s2[i-l1]] -= 1
            if window[s2[i-l1]] == 0:
                window.pop(s2[i-l1])
            # check if matches
            if window == target:
                return True


        return False
        

def main():
    s = Solution()
    cases = [
        ("ab", "eidbaooo"),
        ("ab", "eidboaoo")
    ]
    for case in cases:
        s1, s2 = case
        print(case)
        print(s.checkInclusion(s1, s2))
    

if __name__ == "__main__":
    main()
