from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # find the node
        cur = root
        prev = None
        while cur and cur.val != key:
            prev = cur
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left
        if not cur:
            return root
        # no child, leaf node
        if (not cur.left) and (not cur.right):
            if not prev:
                return None
            if prev.left and prev.left.val == cur.val:
                prev.left = None
            else:
                prev.right = None
            return root
        # replace the node value with largest child in left subtree
        if cur.left:
            nc = cur.left
            prev_nc = cur
            while nc.right:
                prev_nc = nc
                nc = nc.right
        # replace the node value with smallest child in right subtree
        elif cur.right:
            nc = cur.right
            prev_nc = cur
            while nc.left:
                prev_nc = nc
                nc = nc.left
        cur.val = nc.val
        if prev_nc.left and prev_nc.left.val == nc.val:
            if nc.right:
                prev_nc.left = nc.right
            else:
                prev_nc.left = nc.left
        else:
            if nc.left:
                prev_nc.right = nc.left
            else:
                prev_nc.right = nc.right
        return root

root = TreeNode(1)
root.right = TreeNode(2)

sol = Solution()
sol.deleteNode(root, 2)
