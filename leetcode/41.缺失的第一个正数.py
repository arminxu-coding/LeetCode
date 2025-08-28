"""
41. 缺失的第一个正数
https://leetcode.cn/problems/first-missing-positive/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)

        # 哈希表
        # values = set()
        # for num in nums:
        #     values.add(num)
        #
        # for i in range(1, length + 1):
        #     if i not in values:
        #         return i
        # return length + 1

        if 1 not in nums:
            return 1
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = 1

        for i in range(length):
            # 获取当前位置的值，对应应该所处的下标
            num = abs(nums[i])
            nums[num - 1] = -abs(nums[num - 1])

        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1


if __name__ == '__main__':
    solution = Solution()

    print(solution.firstMissingPositive([1, 2, 0]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
