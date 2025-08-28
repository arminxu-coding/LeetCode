"""
73. 矩阵置零
https://leetcode.cn/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # 行列存储
        # rows = set()
        # cols = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        # 标记变量
        row = any(matrix[0][j] == 0 for j in range(n))  # 表示第一行 要变0
        col = any(matrix[i][0] == 0 for i in range(m))  # 表示第一列 要变0

        for i in range(1, m):
            for j in range(1, n):
                # 当前位置为0，那么这一行 这一列都得为0
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                # 如果当前行 或者 当前列为0，那么当前位置就得为0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 第一行得为0
        if row:
            for j in range(n):
                matrix[0][j] = 0

        # 第一列得为0
        if col:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    print(matrix)

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(matrix)
    print(matrix)
