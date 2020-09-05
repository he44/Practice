from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # inorder traversal
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        # get elements
        val_1 = inorder(root1)
        val_2 = inorder(root2)

        # merge the two lists
        ans = []
        n1 = len(val_1)
        n2 = len(val_2)
        p1 = 0
        p2 = 0
        while p1 < n1 and p2 < n2:
            if val_1[p1] <= val_2[p2]:
                ans.append(val_1[p1])
                p1 += 1
            else:
                ans.append(val_2[p2])
                p2 += 1
        ans += (val_1[p1:] + val_2[p2:])
        return ans


                    


