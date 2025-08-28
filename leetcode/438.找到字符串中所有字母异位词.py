"""
438. 找到字符串中所有字母异位词
https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def is_ectopic_words(str1: str, str2: str) -> bool:
            """ 是否为 异位词 """
            return str(sorted(str1)) == str(sorted(str2))

        res = []

        # 方法一：暴力（超时）
        # len1, len2 = len(s), len(p)
        # for i in range(0, len1 - len2 + 1, 1):
        #     sub_s = s[i:i + len2:1]
        #     # 判断 sub_s 和 p 是否为 异位词
        #     if is_ectopic_words(sub_s, p):
        #         res.append(i)

        # 方法二：暴力 + 优化判断是否为 异位词
        s_counts, s_len = [0] * 26, len(s)
        p_counts, p_len = [0] * 26, len(p)
        if p_len > s_len:
            return res
        a = ord('a')
        for i in range(p_len):
            s_counts[ord(s[i]) - a] += 1
            p_counts[ord(p[i]) - a] += 1
        if s_counts == p_counts:
            res.append(0)
        right = p_len
        while right < s_len:
            left = right - p_len + 1
            s_counts[ord(s[left - 1]) - a] -= 1
            s_counts[ord(s[right]) - a] += 1
            if s_counts == p_counts:
                res.append(left)
            right += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams(s="cbaebabacd", p="abc"))
    print(solution.findAnagrams(s="abab", p="ab"))
    print(solution.findAnagrams(s="aa", p="bb"))
