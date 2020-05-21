from typing import *

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        # go to the left most leaf (smallest element)
        while True:
            while root:
                stack.append(root)
                root = root.left

            # examine one element
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            root = root.right
        
        
        

