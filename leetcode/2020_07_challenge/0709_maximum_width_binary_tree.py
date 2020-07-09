from typing import *

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        queue = [(root, 1)]
        while queue:
            level_len = len(queue)
            level_head = queue[0][1]
            #print(level_len, level_head, queue)
            for _ in range(level_len):
                cur, cur_col = queue.pop(0)
                max_width = max(max_width, cur_col - level_head + 1)
                #print(cur.val, cur_col)
                if cur.left:
                    queue.append((cur.left, cur_col * 2))
                if cur.right:
                    queue.append((cur.right, cur_col * 2 + 1))
        return max_width
