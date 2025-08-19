"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
函数 myAtoi(string s) 的算法如下：
空格：读入字符串并丢弃无用的前导空格（" "）
符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
返回整数作为最终结果。

示例 1：
    输入：s = "42"
    输出：42
    解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
    带下划线线的字符是所读的内容，插入符号是当前读入位置。
    第 1 步："42"（当前没有读入字符，因为没有前导空格）
             ^
    第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
             ^
    第 3 步："42"（读入 "42"）
               ^
示例 2：
    输入：s = " -042"
    输出：-42
    解释：
    第 1 步："   -042"（读入前导空格，但忽视掉）
                ^
    第 2 步："   -042"（读入 '-' 字符，所以结果应该是负数）
                 ^
    第 3 步："   -042"（读入 "042"，在结果中忽略前导零）
                   ^
https://leetcode.cn/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        flag = 1
        index = 0
        if s[0] == "-":
            flag = -1
            index = 1
        elif s[0] == "+":
            index = 1

        res = 0
        for i in range(index, len(s)):
            c = s[i]
            if not (48 <= ord(c) <= 57):
                break  # 非数字，直接跳出
            res = res * 10 + int(c)
        if res == 0:
            return 0
        # 确保结果在 32位有符号整数 范围内
        max = 2 ** 31
        res = flag * res
        if res < -max:
            return -max
        elif res > max - 1:
            return max - 1
        return res


if __name__ == '__main__':
    solution = Solution()
    # print(solution.myAtoi("42"))
    # print(solution.myAtoi(" -042"))
    # print(solution.myAtoi("1337c0d3"))
    # print(solution.myAtoi("0-1"))
    # print(solution.myAtoi("words and 987"))
    # print(solution.myAtoi("-91283472332"))
    print(solution.myAtoi("   +0 123"))
