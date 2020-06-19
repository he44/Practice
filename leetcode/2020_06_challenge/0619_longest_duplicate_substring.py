from typing import *

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # return -1 if no duplicate substring of length L)
        def Rabin_Karp(L, base, modulus, n, nums):
            # compute the first hash (h[s[0:L])
            h = 0
            for i in range(L):
                h = (h * base + nums[i]) % modulus
            seen = {h:0}
            magic = pow(base, L, modulus) # (base ** L) % modulus
            for i in range(1, n-L+1):
                h = (h * base - nums[i-1] * magic + nums[i + L -1]) % modulus
                if h in seen:
                    if S[seen[h]:seen[h] + L] == S[i:i+L]:
                        return i
                seen[h] = i
            return -1

        # Step 1: Convert string to interger
        nums = [ord(char) - ord('a') for char in S]
        n = len(S)
        base = 26
        modulus = 2**32
        
        # Step 2: Binary search to find the maximum length
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            # can search for larger
            if Rabin_Karp(mid, base, modulus, n, nums) != -1:
                lo = mid + 1
            else:
                hi = mid - 1

        # return the string
        ll = lo # longest length
        ss = Rabin_Karp(ll - 1, base, modulus, n, nums)
        return S[ss:ss+ll-1]


cases = [
    "banana",
    "abcd"
]

sol = Solution()

for case in cases:
    print(sol.longestDupSubstring(case))
        
