"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
    输入：x = 123
    输出：321
示例 2：
    输入：x = -123
    输出：-321
示例 3：
    输入：x = 120
    输出：21
示例 4：
    输入：x = 0
    输出：0
https://leetcode.cn/problems/reverse-integer/description/
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            flag = 1
        else:
            flag = -1
            x = -x
        res = 0
        while x >= 1:
            num = x % 10
            res = res * 10 + num
            x = int(x / 10)
        if res >= (-2 ** 31) and res <= (2 ** 31) - 1:
            return flag * res
        return 0


if __name__ == '__main__':
    solution = Solution()
    # print(solution.reverse(x=123))
    # print(solution.reverse(x=-123))
    # print(solution.reverse(x=120))
    print(solution.reverse(x=1534236469))
