"""
226. 翻转二叉树
https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        left = self.invertTree(root.left)

        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root
