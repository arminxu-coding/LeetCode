"""
49. 字母异位词分组
https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        # for string in strs:
        #     new_string = str(sorted(string))
        #     if new_string not in res:
        #         res[new_string] = [string]
        #     else:
        #         res[new_string].append(string)
        # return list(res.values())

        for sb in strs:
            counts = [0] * 26
            for char in sb:
                counts[ord(char) - ord('a')] += 1
            tmp = tuple(counts)
            if tmp in res:
                res[tmp].append(sb)
            else:
                res[tmp] = [sb]
        return list(res.values())


if __name__ == '__main__':
    solution = Solution()

    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(solution.groupAnagrams([""]))
    # print(solution.groupAnagrams(["a"]))
