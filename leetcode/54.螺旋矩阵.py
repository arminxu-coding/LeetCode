"""
54. 螺旋矩阵
https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col, m, n = 0, 0, len(matrix), len(matrix[0])
        res, total = [], m * n
        directions, dir_index = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        visited = [[False] * n for _ in range(m)]
        for i in range(total):
            # 当前位置添加
            res.append(matrix[row][col])
            visited[row][col] = True
            # 计算下一个位置，判断方向，确定是否要切位置
            next_row, next_col = row + directions[dir_index][0], col + directions[dir_index][1]
            if not (0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]):
                dir_index = (dir_index + 1) % 4
            row += directions[dir_index][0]
            col += directions[dir_index][1]
        return res


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.spiralOrder(matrix))
