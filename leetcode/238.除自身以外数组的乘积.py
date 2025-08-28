"""
238. 除自身以外数组的乘积
https://leetcode.cn/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        temps = [0] * length  # 代表 i位置之前的所有乘积
        temps[0] = 1
        for i in range(1, length):
            temps[i] = temps[i - 1] * nums[i - 1]
        tmp = 1
        for i in range(length - 1, -1, -1):
            temps[i] = temps[i] * tmp
            tmp *= nums[i]
        return temps


if __name__ == '__main__':
    solution = Solution()

    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
