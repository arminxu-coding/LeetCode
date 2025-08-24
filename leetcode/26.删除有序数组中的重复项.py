"""
26. 删除有序数组中的重复项
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        # i, length = 1, len(nums)
        # while i < length:
        #     if nums[i] == nums[i - 1]:
        #         nums.pop(i)
        #         i -= 1
        #         length -= 1
        #     i += 1
        # return length

        left, right = 1, 1
        while right < len(nums):
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left


if __name__ == '__main__':
    solution = Solution()

    print(solution.removeDuplicates(nums=[1, 1, 2]))
    print(solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
