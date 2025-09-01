"""
114. 二叉树展开为链表
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # 方法一：前序遍历
        # if not root:
        #     return
        # stack = [root]
        # prev = None
        # while len(stack) > 0:
        #     # 获取当前访问节点
        #     curr = stack.pop()
        #     # 如果有前驱节点，让前驱节点指向当前节点
        #     if prev:
        #         prev.right = curr
        #         prev.left = None
        #     # 左右节点，入栈
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)
        #     # 全驱节点为当前节点
        #     prev = curr

        # 方法二：寻找前驱节点
        curr = root
        while curr:
            # 判断当前节点是否有左子树
            if curr.left:  # 有左子树，那么找左子树的前驱节点
                predecessor = next = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                # 前驱节点右指针 指向 当前节点右指针
                predecessor.right = curr.right
                curr.left = None
                curr.right = next
            else:  # 没有左子树，那么直接遍历下一个节点 right
                curr = curr.right
