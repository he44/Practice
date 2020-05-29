from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_recursive(root, edges, onstack):
            if onstack[root]:
                return False
            onstack[root] = True
            for neighbor in edges[root]:
                if not dfs_recursive(neighbor, edges, onstack):
                    onstack[root] = False
                    return False
            onstack[root] = False
            return True

        # Construct the graph
        edges = [[] for x in range(numCourses)]
        for hi, lo in prerequisites:
            edges[lo].append(hi)

        # dfs
        onstack = [False for x in range(numCourses)]
        for i in range(numCourses):
            if not dfs_recursive(i, edges, onstack):
                return False
        return True


def main():
    s = Solution()
    """
    cases = [[2, [[0,1]]]]
    """
    cases = [
        [2, [[1,0]]],
        [2, [[0,1]]],
        [2, [[1,0], [0,1]]],
        [3, []],
        [3, [[1,0], [2,1]]],
        [3, [[1,0], [2,1], [0, 2]]],
        [3, [[1,0], [2,1], [1, 2]]],
        [3, [[0,1], [0,2], [1,2]]],
        [4, [[1,0], [2,3], [3, 2]]]
    ]
    for numCourses, prereq in cases:
        print(s.canFinish(numCourses, prereq))

if __name__ == "__main__":
    main()     
        
