from typing import *


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur is not None:
            if cur.val == val:
                return cur
            elif cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        return cur
