from typing import *

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        cnt = {}
        while True:
            winner, loser = max(arr[0], arr[1]), min(arr[0], arr[1])
            arr[0] = winner
            arr.pop(1)
            arr.append(loser)
            if winner not in cnt:
                cnt[winner] = 1
            else:
                cnt[winner] += 1
            if cnt[winner] == k:
                return winner
        

cases = [
    [[2,1,3,5,4,6,7], 2],
    [[3,2,1], 10],
    [[1,9,8,2,3,7,6,4,5], 7],
    [[1,11,22,33,44,55,66,77,88,99], 1000000000],
    [[1,25,35,42,68,70], 1]
]
        
sol = Solution()
for arr, k in cases:
    print(sol.getWinner(arr, k))


# [2, 1, 3, 5, 4, 6, 7]

# 2 {2:1}
# 3 {3:1}
# 5 {5:1}
# 4 {4:0}
