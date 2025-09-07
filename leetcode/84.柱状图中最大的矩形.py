"""
84. 柱状图中最大的矩形
https://leetcode.cn/problems/largest-rectangle-in-histogram/description/?envType=study-plan-v2&envId=top-100-liked
"""
from math import inf
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, length = 0, len(heights)
        for i in range(length):
            min_height = heights[i]
            for j in range(i, length):
                min_height = min(min_height, heights[j])
                # 求[i,j] 的面积
                res = max(res, min_height * (j - i + 1))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(solution.largestRectangleArea([2, 1, 2]))
