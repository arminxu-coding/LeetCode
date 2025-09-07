"""
279. 完全平方数
https://leetcode.cn/problems/perfect-squares/description/?envType=study-plan-v2&envId=top-100-liked
"""
from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j, minn = 1, inf
            while j * j <= i:
                minn = min(minn, dp[i - j * j])
                j += 1
            dp[i] = minn + 1
        return dp[n]
