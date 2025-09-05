"""
131. 分割回文串
https://leetcode.cn/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked
"""
import copy
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s_len = len(s)
        res = []

        def is_round_text(s: str, left: int, right: int):
            # 检查当前 s[left, right] 是否都为回文
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # 回朔
        # def split(index: int, curr_s: list[str]):
        #     """
        #     从index位置进行切割子串
        #     Args:
        #         index: 子串的起始位置
        #         curr_s: 当前切割到index位置保存的子串
        #     Returns: None
        #     """
        #     if index == s_len:
        #         res.append(copy.deepcopy(curr_s))
        #         return
        #     # 遍历从index往后切割的结尾位置（可以切割自己）
        #     for i in range(index, s_len):
        #         # 判断当前子串是否为回文
        #         if not is_round_text(s, index, i):  # 当前子串不是回文了，那么就没必要继续切割了
        #             continue
        #         # 切割
        #         curr_s.append(s[index: i + 1])
        #         split(i + 1, curr_s)
        #         curr_s.pop()
        #
        # split(0, [])
        # return res

        # 动态规划，dp[i][j] 表示 s[i:j+1] 是否为回文，dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        dp = [[False] * s_len for _ in range(s_len)]
        for j in range(s_len):  # j的位置
            for i in range(0, j + 1):  # i的位置
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        # 在进行回朔
        def dfs(index: int, cur_s: list[int]):
            if index == s_len:
                res.append(copy.deepcopy(cur_s))
                return
            for i in range(index, s_len):
                if dp[index][i]:
                    cur_s.append(s[index:i + 1])
                    dfs(i + 1, cur_s)
                    cur_s.pop()

        dfs(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()

    # print(solution.partition("aab"))
    print(solution.partition("cdd"))
