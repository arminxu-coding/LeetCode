"""
51. N 皇后
https://leetcode.cn/problems/n-queens/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1] * n  # 当前方案每一行 皇后放置位置
        blank = ["."] * n  # 当前行的内容
        cols, diagonal1, diagonal2 = set(), set(), set()

        def generate_line() -> list:
            board = list()
            for i in range(n):  # 代表每一行
                blank[queens[i]] = "Q"
                board.append("".join(blank))
                blank[queens[i]] = "."
            return board

        def dfs(row: int):
            if row == n:
                board = generate_line()
                res.append(board)
                return
            for i in range(n):  # 当前 row行的 每一列
                if i in cols or row - i in diagonal1 or row + i in diagonal2:
                    continue
                queens[row] = i
                cols.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                dfs(row + 1)
                cols.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)

        dfs(0)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))
