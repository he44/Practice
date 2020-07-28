from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recursion(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)
            root_idx = idx_map[val]
            root.right = recursion(root_idx + 1, in_right)
            root.left = recursion(in_left, root_idx - 1)
            return root

        idx_map = {}
        for i in range(len(inorder)):
            idx_map[inorder[i]] = i
        return recursion(0, len(inorder) - 1)
