from typing import *

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Construct a Trie (prefix tree) for all possible words
        # check out 0514_implement_trie.py
        trie = {}
        matched = {}

        for word in words:
            cur = trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                    cur = cur[char]
                else:
                    cur = cur[char]
            #  Note: need to have a "end" char character
            #  to differentiate between search and startswith
            #  inserting "apple" should not make search "app" return True
            cur['$'] = word
        
        # Construct a quick function to check if word in Trie
        # also check out 0514_implement_trie.py
        def search_trie(root, word):
            cur = root
            for char in word:
                if char not in cur:
                    return False
                else:
                    cur = cur[char]
            # if no $, then this is just a prefix to another word
            return ('$' in cur)

        # Backtracking
        h = len(board)
        if h == 0:
            return []
        w = len(board[0])

        def backtracking(r, c, parent_node):
            #print('bc', r, c)
            char = board[r][c]
            cur_node = parent_node[char]
            
            # returns cur_node['$'] if it exists; if not, return False
            word_matched = cur_node.pop('$', False)
            if word_matched and word_matched not in matched:
                matched[word_matched] = 1

            # visited
            board[r][c] = "#"

            neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
            for ro, co in neighbors:
                nr = r + ro
                nc = c + co
                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    continue
                if not board[nr][nc] in cur_node:
                    continue
                backtracking(nr, nc, cur_node)

            board[r][c] = char

        for rr in range(h):
            for cc in range(w):
                if board[rr][cc] in trie:
                    backtracking(rr, cc, trie)

        return [x for x in matched]



cases = [
    ["oath","pea","eat","rain"],
    ["oath","dig","dog","dogs"]
]


sol = Solution()
for case in cases:
    print(sol.findWords([[]], case))
