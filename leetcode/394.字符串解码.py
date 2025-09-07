"""
394. 字符串解码
https://leetcode.cn/problems/decode-string/?envType=study-plan-v2&envId=top-100-liked
"""


class Solution:
    def decodeString(self, s: str) -> str:
        index, length = 0, len(s)
        stack = []

        def is_num(char):
            if ord('1') <= ord(char) <= ord('9'):
                return True
            return False

        def get_str(s: str, index: int, end: str) -> tuple[str, int]:
            left = index
            while index < len(s) and s[index] != end:
                index += 1
            return s[left: index], index

        while index < length:
            if is_num(s[index]):
                # 向后找数值
                num, index = get_str(s, index, '[')
                stack.append(int(num))  # 入栈
            elif s[index] == ']':
                # 弹出，组装新的字符串，直到 '['
                last = stack.pop()
                sub_str = ""
                while last != '[':
                    sub_str = last + sub_str
                    last = stack.pop()
                num = stack.pop()
                stack.append(num * sub_str)
                index += 1
            else:
                stack.append(s[index])
                index += 1

        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
    print(solution.decodeString("abc3[cd]xyz"))
