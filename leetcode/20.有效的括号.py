"""
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        values = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for ch in s:
            if ch in values:
                stack.append(ch)
            else:
                if len(stack) == 0 or values[stack.pop()] != ch:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("["))
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([])"))
    print(solution.isValid("([)]"))
