"""
给你一个字符串 s，找到 s 中最长的 回文 子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
https://leetcode.cn/problems/longest-palindromic-substring/
"""


class Solution:

    def is_round_text(self, s: str):
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) <= 1:
            return s
        res = ""
        # 方法一：暴力左右指针
        # for l in range(len(s)):
        #     r = len(s) - 1
        #     while l <= r:
        #         # 判断是否为回文
        #         temp = s[l: r + 1]
        #         if self.is_round_text(temp) and (r - l + 1) > len(res):
        #             res = temp
        #             break
        #         r -= 1
        # return res

        # 方法二：动态规划
        # 先想清楚转换方程，假设 dp(l,r) 代表子串s[l,r]，如果s[l+1] == s[r-1]这是一个回文 && s[l]==s[r]，那么s[l,r]也是回文
        # dp(l,r) == dp(l+1,r-1) && s[l]==s[r]
        # 1.初始化
        dp: list[list[bool]] = []
        length = len(s)
        for l in range(length):
            dp.append([False] * length)
            dp[l][l] = True

        for L in range(1, length + 1):  # 枚举子穿长度
            for l in range(length):  # 枚举左指针
                # 计算右指针
                r = l + L - 1
                if r >= length:
                    break
                if s[l] != s[r]:
                    dp[l][r] = False
                else:
                    if r - l < 3:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l + 1][r - 1]

                if dp[l][r] and (r - l + 1) > len(res):
                    res = s[l:r + 1]
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("ac"))
    print(solution.longestPalindrome("aaaa"))
    # print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("cbbd"))
    print(solution.longestPalindrome(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))
