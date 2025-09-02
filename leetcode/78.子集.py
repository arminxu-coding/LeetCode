"""
78. 子集
https://leetcode.cn/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked
"""
import copy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_nums = []

        def dfs(cur_index: int, nums: list[int]):
            if cur_index == len(nums):
                res.append(copy.deepcopy(sub_nums))
                return
            # 选取当前元素
            sub_nums.append(nums[cur_index])
            # 继续找下一个元素
            dfs(cur_index + 1, nums)
            # 当前位置元素不选中
            sub_nums.pop()
            # 继续选择下一个元素
            dfs(cur_index + 1, nums)

        dfs(0, nums)
        return res
