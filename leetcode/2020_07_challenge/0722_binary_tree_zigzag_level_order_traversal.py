from typing import *

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        this_level = []
        reverse = True
        while queue:
            level_len = len(queue)
            level_head = queue[0]
            reverse = not reverse
            this_level = []
            for _ in range(level_len):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                this_level.append(cur.val)
            if reverse:
                res.append(this_level[::-1])
            else:
                res.append(this_level)
        return res