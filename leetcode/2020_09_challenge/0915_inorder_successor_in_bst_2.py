from typing import *


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # where can this in-order successor come from?
        # either the smallest child in the right subtree
        # ->right -> left till the end
        # or the parent (if left child itself)
        # or the parent's parent (right child, then parent is left child)
        # right --> left --> left --> left
        
        # case 1 takes precedence over case 2 because it will be a smaller value
        if node.right:
            c1 = node.right
            while c1.left:
                c1 = c1.left
            return c1
        # skip all the (right-going subtree)
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent # either node.parent.left == node or it's None


