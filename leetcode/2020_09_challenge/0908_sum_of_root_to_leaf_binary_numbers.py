from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # bfs with path tracking?
        def bfs(cur, paths):
            if not cur:
                return 0
            paths.append(str(cur.val))
            # base case: leaf node
            if not cur.left and not cur.right:
                num = int(''.join(paths), base=2)
                paths.pop()
                return num
            # move forward
            ans = bfs(cur.left, paths) + bfs(cur.right, paths)
            paths.pop()
            return ans
        paths = []
        return bfs(root, paths)
            



        
