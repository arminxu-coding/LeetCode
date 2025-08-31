"""
48. 旋转图像
https://leetcode.cn/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n == 1:
            return
        # new_matrix = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         new_matrix[j][n - i - 1] = matrix[i][j]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = new_matrix[i][j]

        for i in range(0, n // 2):
            for j in range(0, (n + 1) // 2):
                i1, j1 = j, n - i - 1
                tmp1 = matrix[i1][j1]
                matrix[i1][j1] = matrix[i][j]

                i2, j2 = j1, n - i1 - 1
                tmp2 = matrix[i2][j2]
                matrix[i2][j2] = tmp1

                i3, j3 = j2, n - i2 - 1
                tmp3 = matrix[i3][j3]
                matrix[i3][j3] = tmp2

                matrix[i][j] = tmp3


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    print(matrix)

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix)
    print(matrix)
