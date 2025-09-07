"""
300. 最长递增子序列
https://leetcode.cn/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i] 代表 以num[i]作为最大值结尾，子串最大长度
        res = 1
        for right in range(1, n):
            for left in range(0, right):
                # 从左开始判断，如果当前 nums[left] < nums[right]的话，可以被纳入计算
                if nums[left] < nums[right]:
                    dp[right] = max(dp[right], dp[left] + 1)
            res = max(res, dp[right])
        return res
