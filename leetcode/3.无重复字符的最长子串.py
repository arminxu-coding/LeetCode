"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 双指针
        # if s is None:
        #     return 0
        # length = len(s)
        # if length <= 1:
        #     return length
        # max = 0
        # for i in range(length):
        #     strings = ""
        #     for j in range(i, length):
        #         if s[j] in strings:  # 开始重复了
        #             break
        #         else:
        #             strings += s[j]
        #     max = len(strings) if len(strings) > max else max
        # return max

        # 滑动窗口 + 哈希表
        char_index = {}  # 保持当前滑动窗口的所有单词，key为单词，value代表以当前key作为左边界起点的 索引下标
        max = 0
        left = 0  # 当前滑动窗口的左边界
        for right, char in enumerate(s):
            # 判断当前 char 是否在当前滑动窗口中存在，并且 当前char作为左边界 位置是在窗口后面的
            if char in char_index and char_index[char] >= left:
                # 是了，那么就要以当前 char的后面一位作为新的滑动窗口啊
                left = char_index[char] + 1
            # 以当前 char 作为滑动窗口的左边界
            char_index[char] = right
            # 计算当前左右边界的长度
            length = right - left + 1
            if length > max:
                max = length
        return max


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("au"))
