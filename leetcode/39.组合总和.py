"""
39. 组合总和
https://leetcode.cn/problems/combination-sum/?envType=study-plan-v2&envId=top-100-liked
"""
import copy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        res = []

        # def nums_in(nums: list[int]):
        #     nums.sort()
        #     for items in res:
        #         if len(items) == len(nums):
        #             flag = True
        #             for i in range(len(items)):
        #                 if nums[i] != items[i]:
        #                     flag = False
        #             if flag:
        #                 return True
        #     return False

        def dfs(index: int, cur_nums: list[int], cur_val: int):
            """
            当前位置进行dfs遍历
            Args:
                index: 当前被访问的原属数组的 索引
                cur_nums: 当前被记录下方选择的组合
                cur_val: 当前的target被减去后剩余的值
            Returns: None
            """
            if index >= length:
                return
            if cur_val == 0:
                res.append(copy.deepcopy(cur_nums))
                return

            # 不选
            dfs(index + 1, cur_nums, cur_val)
            # 选择，选择自己之后，还可以选择自己
            if cur_val - candidates[index] >= 0:
                cur_nums.append(candidates[index])
                dfs(index, cur_nums, cur_val - candidates[index])
                cur_nums.pop()

        dfs(0, [], target)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum(candidates=[2, 3, 6, 7], target=7))
