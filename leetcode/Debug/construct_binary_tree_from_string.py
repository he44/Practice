# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import string
from typing import Tuple

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # returns the root constructed from substring
        def recursion(substring: str) -> Tuple[TreeNode, int]:
            cur_node = None
            if substring == "":
                return cur_node
            size = len(substring)
            i = 0
            # substr[val_start:val_end] should give the entire value
            val_start = None
            val_end = None

            while i < size:
                if s[i] in "-0123456789":
                    if val_start is None:
                        val_start = i
                else:
                    if val_end is None:
                        val_end = i
                        cur_node = TreeNode(val=int(substring[val_start:val_end]))
                    if s[i] == ')':
                        return cur_node, i
                    if s[i] == '(':
                        child, last_idx = recursion(substring[i + 1:])
                        i = last_idx
                        if cur_node.left is None:
                            cur_node.left = child
                        else:
                            cur_node.right = child
                i += 1

        root = recursion(s)
        return root


def main():
    sol = Solution()
    test_cases = [
        "4(2(3)(1))(6(5))"
    ]
    for test_case in test_cases:
        sol.str2tree(test_case)


if __name__ == "__main__":
    main()