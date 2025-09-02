"""
131. 分割回文串
https://leetcode.cn/problems/palindrome-partitioning/?envType=study-plan-v2&envId=top-100-liked
"""
import copy
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_round_text(sub_s: list[str]):
            # 检查当前是否都为回文
            for s in sub_s:
                if not s:
                    return False
                s_len = len(s)
                if s_len == 0:
                    return False
                left, right = 0, len(s) - 1
                while left <= right:
                    if s[left] != s[right]:
                        return False
                    left += 1
                    right -= 1
            return True

        def split(str_len: int, sub_s: str, curr_s: list[str], direct: int) -> list[str]:
            sub_s_len = len(sub_s)
            if sub_s_len == 0:
                return copy.deepcopy(curr_s)
            if sub_s_len <= str_len:
                curr_s.append(sub_s)
                return copy.deepcopy(curr_s)
            # 进行切割
            if direct == 1:  # 从前到后
                curr_s.append(sub_s[0:str_len])
                split(str_len, sub_s[str_len:], curr_s, direct)
            elif direct == -1:  # 从后往前
                curr_s.append(sub_s[sub_s_len - 1:sub_s_len - 1 - str_len:-1])
                split(str_len, sub_s[0: sub_s_len - str_len], curr_s, direct)
            return copy.deepcopy(curr_s)

        res = []
        for i in range(len(s)):
            str_len = i + 1
            sub_s = split(str_len, s, [], 1)
            if is_round_text(sub_s):
                res.append(sub_s)
            if len(s) // str_len != 0:
                sub_s_1 = split(str_len, s, [], -1)
                sub_s_1.sort()
                if sub_s_1 != sub_s and is_round_text(sub_s_1):
                    res.append(sub_s_1)

        return res


if __name__ == '__main__':
    solution = Solution()

    # print(solution.partition("aab"))
    print(solution.partition("cdd"))
