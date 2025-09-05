"""
35. 搜索插入位置
https://leetcode.cn/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # 1. 初始化左右指针
        left, right = 0, len(nums) - 1

        # 2. 当 left <= right 时继续查找
        while left <= right:
            # 3. 计算中点索引
            mid = (left + right) // 2

            # 4. 如果中点值正好等于 target，直接返回 mid
            if nums[mid] == target:
                return mid
            # 5. 如果中点值小于 target，说明 target 在右半区
            elif nums[mid] < target:
                left = mid + 1
            # 6. 否则 target 在左半区
            else:
                right = mid - 1

        # 7. 如果跳出循环还没找到 target，
        #    那么 left 就是 target 应插入的位置
        return left
