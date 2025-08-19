"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
示例 1：
    输入：x = 121
    输出：true
示例 2：
    输入：x = -121
    输出：false
    解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：
    输入：x = 10
    输出：false
    解释：从右向左读, 为 01 。因此它不是一个回文数。
https://leetcode.cn/problems/palindrome-number/description/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # 方法一：转字符串，双指针遍历
        # x = str(x)
        # i = 0
        # j = len(x) - 1
        # while i <= j:
        #     if x[i] != x[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True

        # 计算反转数字
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x / 10)

        return x == revertedNumber or x == int(revertedNumber / 10)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
