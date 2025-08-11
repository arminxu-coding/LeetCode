"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。

示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0
解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
https://leetcode.cn/problems/3sum-closest/description/
"""


class Solution:

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # 方法一：暴力
        # length = len(nums)
        # result = 10 ** 7
        # for i in range(0, length):
        #     for j in range(i + 1, length):
        #         for k in range(j + 1, length):
        #             sum = nums[i] + nums[j] + nums[k]
        #             # 当前结果的差值的绝对值 < 上一个结果的插值的绝对值
        #             if abs(target - sum) < abs(target - result):
        #                 result = sum
        # return result

        # 方法二：双指针
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 定义左右指针
            l, r = i + 1, length - 1
            # 左右指针遍历
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return target

                if abs(target - sum) < abs(target - result):  # 当前差值 < 上次差值，说明当前对的
                    result = sum

                if sum > target:  # 当前值 > 上次值，说明当前大了，应该缩小试试
                    k = r - 1  # 为了去重
                    while l < k and nums[k] == nums[r]:
                        k -= 1
                    r = k
                else:  # 当前值 <= 上次值，可以适当增大值
                    k = l + 1
                    while k < r and nums[k] == nums[l]:
                        k += 1
                    l = k
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1)
    print(result)
    result = solution.threeSumClosest(nums=[0, 0, 0], target=1)
    print(result)
    result = solution.threeSumClosest(nums=[4, 0, 5, -5, 3, 3, 0, -4, -5], target=-2)
    print(result)
