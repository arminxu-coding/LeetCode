"""
46. 全排列
https://leetcode.cn/problems/permutations/?envType=study-plan-v2&envId=top-100-liked
"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []

        def back(index: int):
            if index == length - 1:
                res.append(copy.deepcopy(nums))
                return

            for i in range(index, length):
                # 当前位置和目标位置换顺序，指代index位置可以在他和他后面的任何位置
                nums[index], nums[i] = nums[i], nums[index]
                back(index + 1)
                # 不选择
                nums[index], nums[i] = nums[i], nums[index]

        back(0)
        return res

        # def back(curr_nums: list[int]):
        #     if len(curr_nums) == length:
        #         res.append(copy.deepcopy(curr_nums))
        #         return
        #
        #     for num in nums:
        #         # 判断是否被选中了
        #         if num in curr_nums:
        #             continue
        #         # 选择
        #         curr_nums.append(num)
        #         back(curr_nums)
        #         # 不选择
        #         curr_nums.pop()
        #
        # back([])
        # return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
