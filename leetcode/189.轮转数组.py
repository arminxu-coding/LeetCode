"""
189. 轮转数组
https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        if k == 0:
            return

        # temp = []
        # temp[0:k] = nums[length - k:length]
        # temp[k: length] = nums[0:length - k]
        # for i in range(length):
        #     nums[i] = temp[i]

        def reverse(nums: list[int], left: int, right: int):
            while left < right:
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp
                left += 1
                right -= 1

        reverse(nums, 0, length - 1)  # 反转全部
        reverse(nums, 0, k - 1)  # 反转前半部分
        reverse(nums, k, length - 1)  # 反转后半部分


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)

    print(nums)
