from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        edges = [set() for x in range(numCourses)]
        rev_edges = [set() for x in range(numCourses)]
        sources = set(range(numCourses))
        for dst, src in prerequisites:
            edges[src].add(dst)
            rev_edges[dst].add(src)
            if dst in sources:
                sources.remove(dst)
        print(sources)
        # sources: nodes without incoming edges
        # dfs-style algorithm to topological sort
        topological = []
        while sources:
            cur = sources.pop()
            topological.append(cur)
            for neighbor in edges[cur]:
                rev_edges[neighbor].remove(cur)
                if not rev_edges[neighbor]:
                    sources.add(neighbor)
        for dst in rev_edges:
            if dst:
                return []
        return topological


cases = [
    # [2, [[1,0]]],
    # [4, [[1,0],[2,0],[3,1],[3,2]]],
    [3, [[1,0],[1,2],[0,1]]]
]

sol = Solution()

for case in cases:
    print(sol.findOrder(case[0], case[1]))