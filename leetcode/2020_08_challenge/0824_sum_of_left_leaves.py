from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # lr = 0, cur is left child;
        # lr = 1, cur is right child
        def traverse(cur, lr):
            if not cur:
                return 0
            if (not cur.left) and (not cur.right) and lr == 0:
                return cur.val
            return traverse(cur.left, 0) + traverse(cur.right, 1)
        return traverse(root, -1)



                    
