from typing import *

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #  make edges (adjacency matrix)
        neighbors = [[] for x in range(n)]
        edges = [[0 for y in range(n)] for x in range(n)]
        for (src, dst) in connections:
            edges[src][dst] = 1
            edges[dst][src] = -1
            neighbors[src].append(dst)
            neighbors[dst].append(src)
        #print(edges)
        #  dfs
        def dfs(cur, neighbors, edges, visited):
            lc = 0
            #print("cur: ", cur)
            visited[cur] = 1
            for pn in neighbors[cur]:
                if pn not in visited:
                    if edges[cur][pn] == 1:
                        lc += 1
                    lc += dfs(pn, neighbors, edges, visited)
            return lc

        visited = {}
        count = dfs(0, neighbors, edges, visited)

        return count

cases = [
    [6, [[0,1],[1,3],[2,3],[4,0],[4,5]]],
    [5, [[1,0],[1,2],[3,2],[3,4]]],
    [3, [[1,0],[2,0]]]
]

s = Solution()
for n, cns in cases:
    print(s.minReorder(n, cns))

