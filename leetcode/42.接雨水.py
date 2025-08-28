"""
42. 接雨水
https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        res = 0  # 最后的结果

        # 方法一：暴力
        # index = 1  # 表示求第几个位置能够存储的水量
        # while index < length - 1:
        #     left_max = right_max = height[index]
        #     # 向左找最高的柱子（比自己高）
        #     for i in range(0, index):
        #         left_max = max(left_max, height[i])
        #     # 向右找最高的柱子（比自己高）
        #     for i in range(index + 1, length):
        #         right_max = max(right_max, height[i])
        #     # 当前位置的储水量 = 左右两边更矮柱子高度 - 当前高度
        #     res += min(left_max, right_max) - height[index]
        #     index += 1

        # 方法二：动态规划
        # left_maxs = [height[0]] + [0] * (length - 1)
        # for i in range(1, length):
        #     left_maxs[i] = max(left_maxs[i - 1], height[i])
        # right_maxs = [0] * (length - 1) + [height[length - 1]]
        # for i in range(length - 2, -1, -1):
        #     right_maxs[i] = max(right_maxs[i + 1], height[i])
        # for i in range(1, length - 1):
        #     res += min(left_maxs[i], right_maxs[i]) - height[i]

        # 方法三：优化版 双指针
        left, left_max, right, right_max = 0, height[0], length - 1, height[length - 1]
        while left < right:
            # 求其当前计算位置 左边最大和右边最大
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 当前位置，是决定以左边为主 还是以右变为主，决定条件：哪边小哪边为主，计算哪边
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res


if __name__ == '__main__':
    solution = Solution()

    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
