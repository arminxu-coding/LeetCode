"""
LCR 105. 岛屿的最大面积
https://leetcode.cn/problems/ZL6zAn/description/
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res, m, n = 0, len(grid), len(grid[0])

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return 0
            ans = 1
            grid[i][j] = 0  # 探索过了
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                next_i, next_j = i + di, j + dj
                ans += dfs(next_i, next_j)
            return ans

        # 遍历每个节点，从每个节点开始 深度探索（上下左右）
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
