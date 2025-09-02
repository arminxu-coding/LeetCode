"""
124. 二叉树中的最大路径和
https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_sum = -inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def root_max(node: TreeNode) -> int:
            """ 以当前节点为根节点，其最大路径和 """
            if not node:
                return 0

            # 左右子节点最大路径和
            left_max = max(root_max(node.left), 0)
            right_max = max(root_max(node.right), 0)

            # 计算最大路径和
            res = left_max + node.val + right_max
            self.max_sum = max(self.max_sum, res)

            # 当前节点的做大值
            return node.val + max(left_max, right_max)

        root_max(root)
        return self.max_sum
