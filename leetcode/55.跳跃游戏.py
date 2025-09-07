"""
55. 跳跃游戏
https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 方法一：暴力 回溯（超时）
        # def back(nums: list[int], index: int):
        #     if index >= len(nums) - 1:
        #         return True
        #     for jump in range(nums[index], 0, -1):
        #         if back(nums, index + jump):
        #             return True
        #     return False
        # return back(nums, 0)
        max_right, n = nums[0], len(nums)
        for i in range(n):
            # 能不能从这个位置起跳，取决于 之前位置跳跃能不能调到这里
            if i <= max_right:
                # 求从当前位置能跳多远
                max_right = max(max_right, i + nums[i])
                if max_right >= n-1:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
