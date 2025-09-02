"""
102. 二叉树的层序遍历
https://leetcode.cn/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []

        while len(queue) > 0:
            level_size, level_nodes = len(queue), []
            # 当前层 遍历
            while level_size > 0:
                # 弹出 当前层某个节点
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
                level_nodes.append(node.val)
            res.append(level_nodes)
        return res
