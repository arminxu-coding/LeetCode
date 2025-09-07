"""
494. 目标和
https://leetcode.cn/problems/target-sum/description/
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.res = 0

        def dfs(index: int, cur: int):
            if index >= n:
                if cur == target:
                    self.res += 1
                return
            # 加 或 减
            dfs(index + 1, cur + nums[index])
            dfs(index + 1, cur - nums[index])

        dfs(0, 0)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
