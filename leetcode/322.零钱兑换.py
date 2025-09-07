"""
322. 零钱兑换
https://leetcode.cn/problems/coin-change/description/?envType=study-plan-v2&envId=top-100-liked
"""
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        # 初始化dp
        dp[0] = 0
        # 开始计算
        for i in range(1, amount + 1):
            minn = inf
            for coin in coins:
                # 判断当前面值大小
                if i >= coin and dp[i - coin] != -1:
                    minn = min(minn, dp[i - coin] + 1)
            if minn != inf:
                dp[i] = minn
        return dp[amount]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange(coins=[1, 2, 5], amount=11))
    print(solution.coinChange(coins=[2], amount=3))
    print(solution.coinChange(coins=[1], amount=0))
    print(solution.coinChange(coins=[2], amount=1))
    print(solution.coinChange(coins=[1, 2], amount=2))
