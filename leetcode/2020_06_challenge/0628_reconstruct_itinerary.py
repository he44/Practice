from typing import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = {}
        for src, dst in tickets:
            if src not in edges:
                edges[src] = [dst]
            else:
                edges[src].append(dst)
        """
        for node in edges:
            edges[node].sort()
        """

        print(edges)
        stack = ["JFK"]
        route = []
        while stack:
            cur = stack[-1]
            print("cur is ", cur)
            while edges[cur]:
                stack.append(edges[cur].pop())
            route.append(stack.pop())
        return route[::-1]



cases = [
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
]

sol = Solution()
for case in cases:
    print(sol.findItinerary(case))

        


