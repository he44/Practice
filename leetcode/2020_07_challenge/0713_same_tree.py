from typing import *


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def recu(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            return (p.val == q.val) and (recu(p.left, q.left)) and (recu(p.right, q.right))
        return recu(p,q)
