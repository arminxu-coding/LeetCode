"""
17. 电话号码的字母组合
https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    VALUES = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        length = len(digits)
        if length == 0:
            return res

        def backtrack(current: list[str], index: int):
            if len(current) == length:  # 回推强
                res.append("".join(current))
                return

            # 选择
            for char in Solution.VALUES[digits[index]]:
                current.append(char)
                backtrack(current, index + 1)
                current.pop()

        backtrack([], 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations("2"))
    print(solution.letterCombinations(""))
