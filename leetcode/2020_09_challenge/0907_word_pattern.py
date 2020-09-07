from typing import *

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        parts = str.split()
        seen = {}
        recorded = set()
        n = len(parts)
        if n != len(pattern):
            return False

        for i in range(n):
            pat = pattern[i]
            if pat not in seen:
                if parts[i] not in recorded:
                    seen[pat] = parts[i]
                    recorded.add(parts[i])
                else:
                    return False
            elif seen[pat] != parts[i]:
                return False
        return True


cases = [
    ["abba", "dog cat cat dog"],
    ["abba", "dog cat cat fish"],
    ["aaaa", "dog cat cat dog"],
    ["abba", "dog dog dog dog"]
]

sol = Solution()
for pat, s in cases:
    print(sol.wordPattern(pat, s))
        
