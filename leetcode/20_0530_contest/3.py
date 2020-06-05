from typing import *

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #  make edges (adjacency matrix)
        #  so make "edges" a dictionary is much faster than a list
        #  this difference can make my solution TLE
        edges = {(x,y) for x, y in connections}
        neighbors = [[] for x in range(n)]
        for (src, dst) in connections:
            neighbors[src].append(dst)
            neighbors[dst].append(src)
        #print(edges)
        #  dfs
        stack = [0]
        visited = {}
        count = 0
        while stack:
            cur = stack.pop()
            visited[cur] = 1
            #print(cur)
            for pn in neighbors[cur]:
                if pn not in visited:
                    stack.append(pn)
                    # from 0 outward, need to reverse
                    if (cur, pn) in edges:
                        count += 1
        return count

cases = [
    [6, [[0,1],[1,3],[2,3],[4,0],[4,5]]],
    [5, [[1,0],[1,2],[3,2],[3,4]]],
    [3, [[1,0],[2,0]]]
]

s = Solution()
for n, cns in cases:
    print(s.minReorder(n, cns))

