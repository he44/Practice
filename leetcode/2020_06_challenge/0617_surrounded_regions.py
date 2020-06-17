from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h = len(board)
        if h == 0:
            return
        w = len(board[0])
        possible_edges = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[False for x in range(w)] for y in range(h)]
        def dfs(root, board, possible_edges, visited):
            if board[root[0]][root[1]] != 'O':
                return
            stack = [root]
            while stack:
                cur = stack.pop()
                visited[cur[0]][cur[1]] = True
                for pe in possible_edges:
                    nr = pe[0] + cur[0]
                    nc = pe[1] + cur[1]
                    if nr > 0 and nr < h and nc > 0 and nc < w and (not visited[nr][nc]):
                        if board[nr][nc] == 'O': 
                            stack.append((nr,nc))

        # dfs on boarders
        # first and last row
        for c in range(w):
            dfs((0, c), board, possible_edges, visited)
            dfs((h-1, c), board, possible_edges, visited)
        for r in range(1, h-1):
            dfs((r, 0), board, possible_edges, visited)
            dfs((r, w-1), board, possible_edges, visited)

        # find bad ones
        for i in range(h):
            for j in range(w):
                if (not visited[i][j]) and (board[i][j] == 'O'):
                    board[i][j] = 'X'



cases = [
    [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
]

        
sol = Solution()
for case in cases:
    print("Before")
    print(case)
    sol.solve(case)
    print("After")
    print(case)
