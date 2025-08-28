"""
56. 合并区间
https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for i in range(len(intervals)):
        #     for j in range(i, len(intervals)):
        #         if intervals[i][0] > intervals[j][0]:
        #             temp = intervals[i]
        #             intervals[i] = intervals[j]
        #             intervals[j] = temp

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for interval in intervals[1:]:
            last_end = res[-1][1]
            if last_end >= interval[0]:  # 合并
                res[-1] = [res[-1][0], max(last_end, interval[1])]
            else:
                res.append(interval)
        return res


if __name__ == '__main__':
    solution = Solution()

    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
