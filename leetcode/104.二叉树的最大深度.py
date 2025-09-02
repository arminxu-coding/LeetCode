"""
104. 二叉树的最大深度
https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node: TreeNode | None, cur_depth: int) -> int:
            if node is None:
                return cur_depth
            left_depth = depth(node.left, cur_depth + 1)
            right_depth = depth(node.right, cur_depth + 1)
            return max(left_depth, right_depth)

        return depth(root, 0)
