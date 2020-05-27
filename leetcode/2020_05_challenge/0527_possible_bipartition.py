from typing import *
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # return True if there's cycle
        def dfs(root, edges, preds, visited):
            stack = [root]
            while stack:
                cur = stack.pop()
                # for the first node
                if preds[cur-1] not in visited:
                    visited[cur] = 0
                else:
                    visited[cur] = 1 - visited[preds[cur-1]]
                for neighbor in edges[cur-1]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        preds[neighbor-1] = cur
                    else:
                        # conflict between color assignment
                        if neighbor != preds[cur-1] and visited[cur] == visited[neighbor]:
                            return True
            return False
        # build the adjaceny list
        edges = [[] for x in range(N)]
        preds = [0 for x in range(N)]
        for a, b in dislikes:
            edges[a-1].append(b)
            edges[b-1].append(a)

        # need to consider the case when it's a graph with multiple partitions
        # make visited universal to ensure no repeated work (Time-Limite Exceeded if repeated work)
        visited = {}
        for i in range(1, N+1):
            if i in visited:
                continue
            if dfs(i, edges, preds, visited):
                return False
        return True


def main():
    s = Solution()

    cases = [
        [6, [[1,2], [1,3], [2,4], [2,5], [4,6]]],
        [4, [[1,2],[1,3],[2,4]]],
        [3, [[1,2],[1,3],[2,3]]],
        [5, [[1,2],[2,3],[3,4],[4,5],[1,5]]],
        [10, [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]],
        [2, []]
    ]
    for case in cases:
        print(s.possibleBipartition(case[0], case[1]))

if __name__ == "__main__":
    main()    
        
