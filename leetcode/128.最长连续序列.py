"""
128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                current_num = num
                current_len = 1
                while (current_num + 1) in nums_set:
                    current_len += 1
                    current_num += 1
                res = max(res, current_len)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(solution.longestConsecutive([1, 0, 1, 2]))
