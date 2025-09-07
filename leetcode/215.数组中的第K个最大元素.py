"""
215. 数组中的第K个最大元素
https://leetcode.cn/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-100-liked
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # length = len(nums)
        # def quick_find_k(nums: list[int], left: int, right: int, k: int):
        #     """ 正序找到第k个 """
        #     if left == right:  # 找到了
        #         return nums[k]
        #     point, i, j = nums[left], left - 1, right + 1
        #     while i < j:
        #         while True:
        #             i += 1
        #             if nums[i] >= point:
        #                 break
        #
        #         while True:
        #             j -= 1
        #             if nums[j] <= point:
        #                 break
        #         # 一轮下来，已经明确 此时 point <= nums[i]、nums[j] <= point
        #         if i < j:
        #             nums[i], nums[j] = nums[j], nums[i]
        #     # 那么也就是 [left,j] <= point < [j+1, r] 这个一个排序范围
        #     if k <= j:
        #         return quick_find_k(nums, left, j, k)
        #     else:
        #         return quick_find_k(nums, j + 1, right, k)
        # return quick_find_k(nums, 0, length - 1, length - k)

        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quick_select(nums, k)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
