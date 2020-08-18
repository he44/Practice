from typing import *

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for x in range(num_people)]
        next_c = 1
        remaining = candies
        index = 0
        while remaining > next_c:
            ans[index] += next_c
            remaining -= next_c
            index = (index + 1) % num_people
            next_c += 1
            # print(remaining, next_c, ans)
        ans[index] += remaining
        return ans
            

cases = [
    (7, 4),
    (10, 3)
]

# G gifts
# N person

# turn 1: (1 + 2 + ... + N) = (N+1)N/2
# turn 2: (N + 1) + (N + 2) + ... + (N + N) = (N+1)N/2 + N^2 = 3N^2/2 + N/2
# turn 3: 5N^2/2 + N/2
# ...
# turn k: (2k-1)/2 * (N^2) + N/2
# we need to find the maximum k that's still full


sol = Solution()
for case in cases:
    print(sol.distributeCandies(case[0], case[1]))
