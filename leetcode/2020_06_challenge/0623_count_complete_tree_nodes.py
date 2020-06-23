from typing import *

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Return true if node nidx exists at the last level
        # nn, maximum number of nodes
        def exists(nidx, nn, root, height):
            cur = root
            while nn >=2:
                if nidx < nn // 2:
                    cur = cur.left
                else:
                    cur = cur.right
                    nidx -= nn // 2
                nn = nn // 2
            return (cur is not None)

        # get the height of the tree
        height = 0
        cur = root
        while cur is not None:
            cur = cur.left
            height += 1

        if height == 0 and cur is None:
            return 0

        # binary search
        lo = 0
        hi = 2 ** (height-1) - 1
        nn = 2 ** (height-1)

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if exists(mid, nn, root, height):
                lo = mid + 1
            else:
                hi = mid - 1

        # lo here should be the first non-existent node
        # so there are (lo) nodes in the last layer


        return (2 ** (height-1) - 1) + lo


