from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
                
        prev_ans = [1,1]
        ans = [1,1]
        for k in range(2, rowIndex + 1):
            ans = []
            ans.append(1)
            for i in range(k-1):
                ans.append(prev_ans[i] + prev_ans[i+1])
            ans.append(1)
            prev_ans = ans
            # print(k, ans, prev_ans)
        return ans

cases = [
    0, 1, 2, 3, 4, 5, 6, 7
]

sol = Solution()
for case in cases:
    print(case, sol.getRow(case))


