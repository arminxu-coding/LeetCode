"""
416. 分割等和子集
https://leetcode.cn/problems/partition-equal-subset-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 方法一：暴力 超时
        target, n = sum(nums), len(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        # 回溯搜索
        def dfs(index: int, curr_sum: int) -> bool:
            if curr_sum == target:
                return True
            elif curr_sum > target:  # 已经超过了，没必要选择了
                return False
            if index >= n:
                return False
            # 选择，或者不选
            if dfs(index + 1, curr_sum + nums[index]):
                return True
            if dfs(index + 1, curr_sum):
                return True
            return False
        return dfs(0, 0)

