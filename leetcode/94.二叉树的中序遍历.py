"""
94. 二叉树的中序遍历
https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []

        def inorder(node: TreeNode | None, res: List[int]):
            if node is None:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

        inorder(root, res)
        return res
