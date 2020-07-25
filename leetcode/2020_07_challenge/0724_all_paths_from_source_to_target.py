from typing import *


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        target = len(graph) - 1

        all_paths = []
        
        def backtrack(cur, target, cur_path):
            cur_path.append(cur)
            if cur == target:
                one_ans = cur_path.copy()
                all_paths.append(one_ans)
                cur_path.pop()
                return
            for neighbor in graph[cur]:
                backtrack(neighbor, target, cur_path)
            cur_path.pop()

        cur_path = []
        backtrack(start, target, cur_path)
        return all_paths

cases = [
    [[1,2], [3], [3], []],
    [[]]
]

sol = Solution()
for graph in cases:
    print(sol.allPathsSourceTarget(graph))