# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        node = root
        for i in range(1, len(preorder)):
            parent = stack[-1]
            child = TreeNode(preorder[i])
            # make sure the parent
            while stack and stack[-1].val < child.val:
                parent = stack.pop()

            # build the tree
            if child.val > parent.val:
                parent.right = child
            else:
                parent.left = child

            stack.append(child)
        return root

