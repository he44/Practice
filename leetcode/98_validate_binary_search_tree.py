from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(root, c_min, c_max):
            if not root:
                return True
            if root.val <= c_min or root.val >= c_max:
                return False
            return (
                recursion(root.left, c_min, min(c_max, root.val)) and
                recursion(root.right, max(c_min, root.val), c_max)
            )
        return recursion(root, float('-inf'), float('inf'))