from typing import *

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def update_pattern(s):
            return s + '1' + (''.join([str(1 - int(k)) for k in s]))[::-1]
        sp2 = '0'
        if n == 1:
            return sp2[k-1]
        sp1 = update_pattern(sp2)
        for i in range(n-1):
            sp2 = sp1
            sp1 = update_pattern(sp1)
        return sp1[k-1]

cases = [
    (3,1),
    (4,11),
    (1,1),
    (2,3)
]

sol = Solution()
for n, k in cases:
    print(sol.findKthBit(n,k))


# s1 = '0'
# si = si-1 + '1' + reverse(invert(si-1))

# s1 = '0'
# invert(s1) = '1'
# reverse(invert(s1)) = '1'
# s2 = '011'

# invert(s2) = '100'
# reverse(invert(s2)) = '001'
# s3 = '0111001'
