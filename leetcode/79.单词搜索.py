"""
79. 单词搜索
https://leetcode.cn/problems/word-search/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def dfs(i: int, j: int, index: int) -> bool:
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < m and 0 <= next_j < n:
                    if (next_i, next_j) not in visited:
                        if dfs(next_i, next_j, index + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()

    print(solution.exist(board=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word="ABCCED"))
