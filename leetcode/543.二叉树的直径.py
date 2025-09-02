"""
543. 二叉树的直径
https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def depth(node: TreeNode | None) -> int:
            if not node:
                return 0
            # 求去左子树、右子树 深度
            left = depth(node.left)
            right = depth(node.right)

            # 判断当前是否为最大值，是的话更新
            self.res = max(left + right, self.res)
            return max(left, right) + 1

        depth(root)
        return self.res
