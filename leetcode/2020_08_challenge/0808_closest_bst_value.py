from typing import *

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        cur = root
        while cur:
            # update closest
            new_diff = abs(cur.val - target) 
            closest = cur.val if new_diff < abs(closest - target) else closest
            # binary search
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
        return closest

            
                    
