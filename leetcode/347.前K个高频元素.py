"""
347. 前 K 个高频元素
https://leetcode.cn/problems/top-k-frequent-elements/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key_counts = {}  # 统计
        for num in nums:
            key_counts[num] = key_counts.get(num, 0) + 1
        # 排序
        key_counts = [item for item in key_counts.items()]
        key_counts.sort(key=lambda x: x[1])

        return [key for key, value in key_counts[-k:]]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    # print(solution.topKFrequent(nums=[3, 0, 1, 0], k=1))
    # print(solution.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))
    print(solution.topKFrequent(nums=[1], k=1))
