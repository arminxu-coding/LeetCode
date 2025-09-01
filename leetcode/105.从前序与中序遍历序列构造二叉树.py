"""
105. 从前序与中序遍历序列构造二叉树
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree(
                preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int
        ) -> Optional[TreeNode]:
            if preorder_left > preorder_right:
                return None
            # 当前跟节点
            root = TreeNode(preorder[preorder_left])
            # 构建当前左子树
            val_index = index[preorder[preorder_left]]
            left_tree_count = val_index - inorder_left  # 左子树节点个数，用于计算 前序序列坐标范围

            root.left = build_tree(
                preorder_left + 1,
                preorder_left + left_tree_count,
                inorder_left,
                val_index - 1
            )
            root.right = build_tree(
                preorder_left + left_tree_count + 1,
                preorder_right,
                val_index + 1,
                inorder_right
            )
            return root

        index = {item: i for i, item in enumerate(inorder)}
        return build_tree(0, len(preorder) - 1, 0, len(preorder) - 1)


if __name__ == '__main__':
    solution = Solution()

    root = solution.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])

    print(root)
