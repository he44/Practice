from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        rl_sum = 0
        stack = [(root, 0)]
        while stack:
            cur, cv = stack.pop()
            #print(cur.val, cv)
            if cur is not None:
                cv = cur.val + cv * 10
                # leaf node, just addes to answer (with parents accumulated)
                if cur.left is None and cur.right is None:
                    rl_sum += cv
                else:
                    # last in first out
                    stack.append((cur.right, cv))
                    stack.append((cur.left, cv))
        return rl_sum


root = TreeNode(val=4)
root.left = TreeNode(val=9)
root.right = TreeNode(val=0)
root.left.left = TreeNode(val=5)
root.left.right = TreeNode(val=1)
print(root.val)
sol = Solution()
print(sol.sumNumbers(root))
