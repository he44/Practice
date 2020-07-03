from typing import *

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, cur_level, levels):
            if not node:
                return
            if cur_level == len(levels):
                levels.append([node.val])
            else:
                levels[cur_level].append(node.val)
            dfs(node.left, cur_level + 1, levels)
            dfs(node.right, cur_level + 1, levels)
        levels = []
        dfs(root, 0, levels)
        return levels[::-1]

