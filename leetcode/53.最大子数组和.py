"""
53. 最大子数组和
https://leetcode.cn/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)

        # 暴力
        # max_sum = -999999999999999
        # for i in range(length):
        #     sum = 0
        #     for j in range(i, length):
        #         sum += nums[j]
        #         max_sum = max(max_sum, sum)

        max_sum = prev = nums[0]
        for num in nums[1:]:
            prev = max(prev + num, num)
            if max_sum < prev:
                max_sum = prev

        return max_sum


if __name__ == '__main__':
    solution = Solution()

    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([1]))
    print(solution.maxSubArray([-1]))
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
