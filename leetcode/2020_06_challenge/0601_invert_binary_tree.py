from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #  base case: not a node
        if root is None:
            return
        #  invert children
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        #  invert current level
        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root

s = Solution()

