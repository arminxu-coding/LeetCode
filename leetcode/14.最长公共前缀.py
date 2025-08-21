"""
14. 最长公共前缀
https://leetcode.cn/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = len(strs[0])
        while length > 0:
            first = str(strs[0][0:length])
            flag = True
            for string in strs[0:]:
                if not string.startswith(first):
                    flag = False
                    break
            if flag:
                return first
            length -= 1
        return ""


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
