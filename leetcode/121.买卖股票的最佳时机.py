"""
121. 买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-100-liked
"""
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        # for i in range(n):
        #     # i天买，j天买
        #     max_index = i
        #     for j in range(i + 1, n):
        #         # 找最大值
        #         if prices[j] > prices[max_index]:
        #             max_index = j
        #     res = max(res, prices[max_index] - prices[i])
        # return res

        min_price = inf
        for i in range(n):
            if prices[i] < min_price:  # 当前价格是否最低，考虑买入
                min_price = prices[i]
            elif prices[i] - min_price > res:
                res = prices[i] - min_price
        return res
