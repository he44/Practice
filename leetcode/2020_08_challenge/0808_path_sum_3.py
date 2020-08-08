from typing import *

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(cur_node, cur_sum):
            count = 0
            if not cur_node:
                return count

            cur_sum += cur_node.val
            if cur_sum == sum:
                count += 1

            if cur_sum - sum in prefix_sums:
                count += prefix_sums[cur_sum - sum]
            if cur_sum in prefix_sums:
                prefix_sums[cur_sum] += 1
            else:
                prefix_sums[cur_sum] = 1

            count += preorder(cur_node.left, cur_sum)
            count += preorder(cur_node.right, cur_sum)

            prefix_sums[cur_sum] -= 1
            return count
            
        prefix_sums = {}
        count = preorder(root, 0)
        return count


                    
