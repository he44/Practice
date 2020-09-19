from typing import *


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        root = "123456789"
        min_len = len(str(low))
        max_len = len(str(high))
        ans = []
        for length in range(min_len, max_len + 1):
            for start in range(len(root) - length + 1):
                candidate = int(root[start:start + length])
                if low <= candidate <= high:
                    ans.append(candidate)
        return ans

cases = [
    (100, 300),
    (1000, 13000)
]

sol = Solution()
for low, high in cases:
    print(sol.sequentialDigits(low, high))
        
