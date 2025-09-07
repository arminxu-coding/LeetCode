"""
198. 打家劫舍
https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n  # dp[i] 代表我走到这一家 我最多能赚多少钱
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # 都到第二家，我要不偷第一家，要不偷第二家，哪个大我偷谁
        index = 2
        while index < n:
            # 偷不偷
            cur = dp[index - 2] + nums[index]
            if cur > dp[index - 1]:
                dp[index] = cur
            else:
                dp[index] = dp[index - 1]
            index += 1
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([2, 1, 1, 2]))
    print(solution.rob([1, 2]))
