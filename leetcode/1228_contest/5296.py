# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTreeElements(self, root):
        if root == None:
            return []
        #  base case, root is leaf node
        if root.left == None and root.right == None:
            return [root.val]
        #  recursion
        return self.getTreeElements(root.left) + [root.val] + self.getTreeElements(root.right)


    def getAllElements(self, root1, root2):
        #  get all elements from tree 1 and tree 2 separately
        elements1 = self.getTreeElements(root1)
        elements2 = self.getTreeElements(root2)
        all = elements1 + elements2
        return sorted(all)
        
