"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：
输入：s = "A", numRows = 1
输出："A"
https://leetcode.cn/problems/zigzag-conversion/description/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index = 0
        flag = 1
        str_rows = {}
        for c in s:
            str_rows[index] = str_rows[index] + c if index in str_rows else c
            index = index + flag
            if index == numRows - 1:
                flag = -1
            elif index == 0:
                flag = 1

        res = ""
        for value in str_rows.values():
            res += value
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s="PAYPALISHIRING", numRows=3))
    print(solution.convert(s="PAYPALISHIRING", numRows=4))
