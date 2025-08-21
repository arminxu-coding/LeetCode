"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

示例 1：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
    解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：
    输入：height = [1,1]
    输出：1
https://leetcode.cn/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        length = len(height)
        res = 0
        # 方法一：双指针（会超时）
        # for i in range(length):
        #     for j in range(length - 1, i, -1):
        #         if height[i] < height[j]:
        #             tmp = height[i] * (j - i)
        #         else:
        #             tmp = height[j] * (j - i)
        #         res = tmp if tmp > res else res

        # 方法二：双指针（双向缩小，动小的）
        i = 0
        j = length - 1
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            # 动小的
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea([1, 1]))
