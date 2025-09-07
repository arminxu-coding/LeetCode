"""
739. 每日温度
https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index, length, stack = 1, len(temperatures), []
        res = [0] * length
        stack.append((0, temperatures[0]))
        while index < length:
            while len(stack) > 0:
                # 当前位置如果比栈顶要大，说明了，栈顶位置元素找到了第一个比它温度更高的位置了
                top_index, top_value = stack[-1]
                if temperatures[index] > top_value:
                    res[top_index] = index - top_index
                else:
                    break
                # 弹出栈顶，再次判断新栈顶
                stack.pop()
            # 当前元素入栈
            stack.append((index, temperatures[index]))
            index += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
