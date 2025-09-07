"""
139. 单词拆分
https://leetcode.cn/problems/word-break/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 代表s[0,i)是否满足 拆分子串都在wordDict中
        dp[0] = True
        for right in range(n):
            left = 0
            while left <= right:
                # s[0,left] && s[left, right]在wordDict中
                if dp[left] and s[left:right + 1] in wordDict:
                    dp[right + 1] = True
                    break
                left += 1
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
