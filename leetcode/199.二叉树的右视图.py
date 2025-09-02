"""
199. 二叉树的右视图
https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
            res.append(level_nodes[-1])
        return res
