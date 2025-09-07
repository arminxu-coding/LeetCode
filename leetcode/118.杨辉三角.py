"""
118. 杨辉三角
https://leetcode.cn/problems/pascals-triangle/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(1, numRows + 1):
            row, index, right = [0] * n, 1, n - 1
            row[0] = row[right] = 1
            while index < right:
                # 计算当前位置值
                last_row = n - 2
                row[index] = res[last_row][index - 1] + res[last_row][index]
                index += 1
            res.append(row)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
