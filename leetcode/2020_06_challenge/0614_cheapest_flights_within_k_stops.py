from typing import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        DP
        """
        # dps[a][b] denotes shortest path from src to b using at most k edges
        # in this problem, k stops means k+1 edges
        dps = [[0 for y in range(K+2)] for x in range(n)]
        # Base case
        for node in range(n):
            dps[node][0] = float('inf')
        for i in range(K+2):
            dps[src][0] = 0
    
        """
        Build the graph
        """
        edges = [[] for x in range(n)]
        rev_edges = [[] for x in range(n)]
        edge_weight = {}
        for a,b,w in flights:
            edges[a].append(b)
            edge_weight[(a,b)] = w
            rev_edges[b].append(a)

        """
        Recursion
        """
        for i in range(1, K + 2):
            for node in range(n):
                this_min = dps[node][i-1]
                for un in rev_edges[node]:
                    this_min  = min(this_min, dps[un][i-1] + edge_weight[(un, node)])
                dps[node][i] = this_min

        if dps[dst][K+1] == float('inf'):
            return -1
        return dps[dst][K+1] 


sol = Solution()

cases = [
    #[3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1],
    #[3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0],
    [5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1]
]


for case in cases:
    n, flights, src, dst, K = case
    print(sol.findCheapestPrice(n, flights, src, dst, K))

            



        
