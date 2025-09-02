"""
54. 螺旋矩阵
https://leetcode.cn/problems/spiral-matrix/solutions/275393/luo-xuan-ju-zhen-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, row, col = len(matrix), len(matrix[0]), 0, 0
        visited = [[False] * n] * m
        total_num = m * n
        res = [0] * total_num
        directions, direction_index = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        for i in range(total_num):
            # 获取当前位置，加入
            res[i] = matrix[row][col]
            visited[row][col] = True
            # 计算下一个位置
            next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
            # 校验位置合法性
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or visited[next_row][next_col]:
                direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]

        return res


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().spiralOrder(matrix))
