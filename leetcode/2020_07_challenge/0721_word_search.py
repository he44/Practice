from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, visited, chars):
            # print('something', x, y, chars)
            # base case: char is empty, return True
            if len(chars) == 0:
                return True
            # base case: x, y out of bound, return False
            if x < 0 or y < 0 or x >= h or y >= w:
                return False
            # base case: already visited or char not matching
            if visited[x][y] or board[x][y] != chars[0]:
                return False
            # explore neighbors
            visited[x][y] = True
            neighbor_idx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xi, yi in neighbor_idx:
                xn = x + xi
                yn = y + yi
                if backtrack(xn, yn, visited, chars[1:]):
                    return True
            visited[x][y] = False
            return False
        h = len(board)
        w = len(board[0])
        visited = [[False for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):
                if backtrack(r, c, visited, word):
                    return True
        return False


cases = [
    [
        [["a"]], "a"
    ],
    [
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ],
        "ABCCED"
    ],
    [
        [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "SEE"
    ],
    [
        [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "ABCB"
    ],
    [
        [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],
        "aaaaaaaaaaaaa"
    ]
]

sol = Solution()
for board, word in cases:
    print(sol.exist(board, word))