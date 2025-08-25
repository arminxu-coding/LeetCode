"""
283. 移动零
https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 方法一：复制数组
        # new_nums = []
        # zero_nums = []
        # for num in nums:
        #     if num == 0:
        #         zero_nums.append(0)
        #     else:
        #         new_nums.append(num)
        # new_nums.extend(zero_nums)
        # nums[:] = new_nums

        # 方法二：双指针
        # def swap_left_append_0(i: int, j: int):
        #     for index in range(i, j + 1):
        #         nums[index - 1] = nums[index]
        #     nums[j] = 0
        #
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     if nums[l] == 0:
        #         swap_left_append_0(l + 1, r)
        #         r -= 1
        #     else:
        #         l += 1

        # 方法三：双指针 交换
        l = 0  # 左右指针代表 0左右边界
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)
