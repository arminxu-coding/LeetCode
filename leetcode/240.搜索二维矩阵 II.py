"""
240. 搜索二维矩阵 II
https://leetcode.cn/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     # 本行开启二分查找
        #     left, right = 0, n - 1
        #     while left <= right:
        #         mid = (right + left) // 2
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return False

        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


if __name__ == '__main__':
    solution = Solution()

    print(
        solution.searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
            target=5
        )
    )

    print(
        solution.searchMatrix(
            [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
            target=20
        )
    )

    print(
        solution.searchMatrix(
            [[-1, 3]],
            3
        )
    )
