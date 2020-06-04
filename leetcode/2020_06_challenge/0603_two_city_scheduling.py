from typing import *

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        n = len(costs) // 2
        min_cost = 0
        for i in range(n):
            min_cost += (costs[i][0] + costs[i+n][1])
        return min_cost


s = Solution()
cases = [[[10,20],[30,200],[400,50],[30,20]]]

for costs in cases:
    print(s.twoCitySchedCost(costs))

        
