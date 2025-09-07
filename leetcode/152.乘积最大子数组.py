"""
152. 乘积最大子数组
https://leetcode.cn/problems/maximum-product-subarray/description/?envType=study-plan-v2&envId=top-100-liked
"""
from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = minn = res = nums[0]
        for i in range(1, n):
            mx,mn = maxx, minn
            maxx = max(mx * nums[i], max(nums[i], nums[i] * mn))
            minn = min(mn * nums[i], min(nums[i], nums[i] * mx))
            res = max(res, maxx)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))
    print(solution.maxProduct([-2]))
    print(solution.maxProduct([-2, 3, -4]))
    print(solution.maxProduct([-4,-3,-2]))

