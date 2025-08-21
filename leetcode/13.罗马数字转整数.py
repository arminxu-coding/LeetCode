"""
13. 罗马数字转整数
https://leetcode.cn/problems/roman-to-integer/description/
"""


class Solution:
    VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        for i, ch in enumerate(s):
            # 获取当前字符对应的 数值
            val = Solution.VALUES[ch]
            if i < n - 1 and val < Solution.VALUES[s[i + 1]]:
                res = res - val
            else:
                res = res + val
        return res


if __name__ == '__main__':
    solution = Solution()
    # print(solution.romanToInt(s="III"))
    print(solution.romanToInt(s="IV"))
    print(solution.romanToInt(s="IX"))
    print(solution.romanToInt(s="LVIII"))
    print(solution.romanToInt(s="MCMXCIV"))
