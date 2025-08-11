"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 方法一，for循环 采用双指针遍历
        # for index1 in range(0, len(nums)):
        #     for index2 in range(index1 + 1, len(nums)):
        #         if nums[index1] + nums[index2] == target:
        #             return [index1, index2]
        # return []

        # 方法二，哈希
        diffs = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in diffs:
                return [diffs[value], index]
            else:
                diffs[num] = index
        return []


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum(nums=[2, 7, 11, 15], target=9)
    print(result)
    result = solution.twoSum(nums=[3, 2, 4], target=6)
    print(result)
    result = solution.twoSum(nums=[3, 3], target=6)
    print(result)
