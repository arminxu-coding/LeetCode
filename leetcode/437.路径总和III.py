"""
437. 路径总和 III
https://leetcode.cn/problems/path-sum-iii/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 方法一：暴力，超时
        # if not root:
        #     return 0
        # paths_list = []
        #
        # # 获取所有的paths
        # def get_path(node: TreeNode, curr_path: list[int]):
        #     if not node.left and not node.right:
        #         return copy.deepcopy(curr_path)
        #
        #         # 遍历左右节点节点
        #     if node.left:
        #         curr_path.append(node.left.val)
        #         paths_list.append(get_path(node.left, curr_path))
        #         curr_path.pop()
        #
        #     if node.right:
        #         curr_path.append(node.right.val)
        #         paths_list.append(get_path(node.right, curr_path))
        #         curr_path.pop()
        #
        #     return copy.deepcopy(curr_path)
        #
        # nodes = []
        #
        # def pre_order(node: TreeNode):
        #     if not node:
        #         return
        #     nodes.append(node)
        #     pre_order(node.left)
        #     pre_order(node.right)
        #
        # pre_order(root)
        # for node in nodes:
        #     paths_list.append(get_path(node, [node.val]))
        # count = 0
        # for paths in paths_list:
        #     sum = 0
        #     for num in paths:
        #         sum += num
        #     if sum == targetSum:
        #         count += 1
        # return count

        # 方法二：dfs
        # def root_sum(root: TreeNode, sum: int) -> int:
        #     if not root:
        #         return 0
        #     ret = 0
        #     if root.val == sum:
        #         ret += 1
        #     ret += root_sum(root.left, sum - root.val)
        #     ret += root_sum(root.right, sum - root.val)
        #     return ret
        #
        # if not root:
        #     return 0
        # ret = root_sum(root, targetSum)
        # ret += self.pathSum(root.left, targetSum)
        # ret += self.pathSum(root.right, targetSum)
        # return ret

        # 方法三：前缀树
        def dfs(node: Optional[TreeNode], presum: int) -> int:
            """
            深度优先搜索，返回到达当前节点可以得到满足条件的路径
            @param node: 当前节点
            @param presum: 根节点到当前节点的路径
            @return: 以当前节点为最后一个节点的，节点和等于目标和的路径数
            """
            if not node: return 0  # 空节点，满足条件路径数为0
            presum += node.val  # 更新节点和

            path_cnt = presum_counts.get(presum - targetSum, 0)  # 从哈希表中获取能和presum配对的前缀和个数
            presum_counts[presum] = presum_counts.get(presum, 0) + 1  # 将当前前缀和加入哈希表
            path_cnt += dfs(node.left, presum) + dfs(node.right, presum)  # 递归处理左右子树
            presum_counts[presum] -= 1  # 这个节点所在的路径都处理完了，这个前缀和也就没用了

            return path_cnt  # 返回总路径数

        presum_counts = {0: 1}  # 记录当前路径上出现的前缀和以及数量, 有一个默认的前缀和0
        return dfs(root, 0)  # 从根节点开始搜索


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(10)
    left = TreeNode(5)
    left.left = TreeNode(3, TreeNode(3), TreeNode(-2))
    left.right = TreeNode(2, None, TreeNode(1))

    right = TreeNode(-3)
    right.right = TreeNode(11)

    root.left = left
    root.right = right

    # root = TreeNode(1)

    res = solution.pathSum(root, 8)

    print(res)
