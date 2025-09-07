"""
45. 跳跃游戏 II
https://leetcode.cn/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        # right = n - 1
        # count = 0
        # while right > 0:
        #     # 从 [0, right - 1]，看最远谁能跳跃到 right 位置
        #     left = right
        #     for i in range(right - 1, -1, -1):
        #         # 判断这个位置是否可以跳跃到right
        #         if i + nums[i] >= right:
        #             left = i
        #     # 此时新的 right 为 left
        #     right = left
        #     count += 1
        # return count

        count, max_right, end = 0, 0, 0
        for i in range(n - 1):
            # 从[0,i]某个位置跳，能跳最远位置
            max_right = max(max_right, i + nums[i])
            if i == end:
                # 从[end,i]中，最远位置 是只要一次就能跳跃到
                end = max_right
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2, 3, 1, 1, 4]))
