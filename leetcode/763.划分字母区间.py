"""
763. 划分字母区间
https://leetcode.cn/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked
"""
from operator import index
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n, res = len(s), []
        words = {}  # 记录每个单词的最右下标
        for i in range(n):
            words[s[i]] = i
        # 尝试遍历
        index = 0
        while index < n:
            # 定义左边界
            left, right = index, words[s[index]]
            # 让我们从 [left, right] 不断移动，并且不断扩充 right
            while index <= right:
                right = max(right, words[s[index]])
                index += 1
            # 此时 [left, right] 就是我们的子串
            res.append(right - left + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.partitionLabels("ababcbacadefegdehijhklij"))
    print(solution.partitionLabels("eccbbbbdec"))
