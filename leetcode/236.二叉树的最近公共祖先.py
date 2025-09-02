"""
236. 二叉树的最近公共祖先
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Solution(self):
        self.parent = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 方法一：dfs递归搜索，不好理解
        # def dfs_search(root: TreeNode, p: 'TreeNode', q: 'TreeNode') -> bool:
        #     """ 判断root是否为 q或者p 的祖先节点 """
        #     if root is None:
        #         return False
        #     left = dfs_search(root.left, p, q)
        #     right = dfs_search(root.right, p, q)
        #
        #     if (left and right) or ((root.val == p.val or root.val == q.val) and (left or right)):
        #         self.parent = root
        #     return left or right or (root.val == p.val or root.val == q.val)
        #
        # dfs_search(root, p, q)
        # return self.parent

        # 方法二：哈希表存储父节点
        node_parent_map: dict[int, TreeNode] = {}

        def dfs(node: TreeNode):
            if node.left:
                node_parent_map[node.left.val] = node
                # 递归遍历左子树
                dfs(node.left)
            if node.right:
                node_parent_map[node.right.val] = node
                dfs(node.right)

        dfs(root)
        visited_nodes = set()  # 被访问过的父节点
        # 具有了父节点关系，找到p节点
        while p:
            visited_nodes.add(p.val)
            p = node_parent_map.get(p.val)  # 找父节点
        while q:
            if q.val in visited_nodes:
                return q
            q = node_parent_map.get(q.val)
        return None
