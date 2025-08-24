"""
22. 括号生成
https://leetcode.cn/problems/generate-parentheses/description/
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(stack: list[str], left: int, right: int):
            if len(stack) == 2 * n:
                res.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                backtrack(stack, left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(stack, left, right + 1)
                stack.pop()

        backtrack([], 0, 0)

        return res


if __name__ == '__main__':
    solution = Solution()

    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(1))
    print(solution.generateParenthesis(2))
