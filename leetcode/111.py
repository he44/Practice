# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def minD(cur):
            #  not existing
            if cur is None:
                return 0
            #  leaf node
            if cur.left is None and cur.right is None:
                return 1
            #  recursion (add shortest path from this node's child to any leaf)
            elif cur.left is not None and cur.right is not None:
                rec = min(minD(cur.left), minD(cur.right))
                return rec + 1
            elif cur.left is not None:
                return minD(cur.left) + 1
            elif cur.right is not None:
                return minD(cur.right) + 1
                
        return minD(root)

    
