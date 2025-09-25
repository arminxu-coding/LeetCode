"""
165. 比较版本号
https://leetcode.cn/problems/compare-version-numbers/description/
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers_list_1 = version1.split(".")
        vers_list_2 = version2.split(".")

        len1, len2 = len(vers_list_1), len(vers_list_2)
        max_len = max(len1, len2)
        for i in range(max_len):
            # 取当前版本号
            ver1, ver2 = 0, 0
            if i < len1:
                ver1 = int(vers_list_1[i])
            if i < len2:
                ver2 = int(vers_list_2[i])
            if ver1 < ver2:
                return -1
            elif ver1 > ver2:
                return 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.compareVersion(version1="1.2", version2="1.10"))
    print(solution.compareVersion(version1="1.01", version2="1.001"))
    print(solution.compareVersion(version1="1.0", version2="1.0.0.0"))
