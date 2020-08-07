from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        all_nodes = []
        stack = [(root, 0, 0)]
        while stack:
            cur, cx, cy = stack.pop()
            all_nodes.append((cur.val, cx, cy))
            if cur.left:
                stack.append((cur.left, cx-1, cy-1))
            if cur.right:
                stack.append((cur.right, cx+1, cy-1))

        all_nodes = sorted(all_nodes, key = lambda x: (x[1], -x[2], x[0]))

        ans = []
        prev = None
        this_ans = []
        for item in all_nodes:
            if prev is None or prev == item[1]:
                this_ans.append(item[0])
            else:
                ans.append(this_ans)
                this_ans = [item[0]]
            prev = item[1]
        ans.append(this_ans)
        return ans
                
