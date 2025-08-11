"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
https://leetcode.cn/problems/add-two-numbers/description/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def m1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 遍历l1 和 l2
        res = ListNode()
        node = res
        next = 0
        while l1 and l2:
            node.val = l1.val + l2.val + next
            if node.val >= 10:
                next = 1
            else:
                next = 0
            node.val = node.val % 10
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        while l1:
            node.val = l1.val + next
            if node.val >= 10:
                next = 1
            else:
                next = 0
            node.val = node.val % 10
            l1 = l1.next
            if l1:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        while l2:
            node.val = l2.val + next
            if node.val >= 10:
                next = 1
            else:
                next = 0
            node.val = node.val % 10
            l2 = l2.next
            if l2:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        if next == 1:
            node.next = ListNode(next)
        return res

    def m2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 方法二：简介代码
        dummy = ListNode(0)
        carry = 0
        current = dummy
        while l1 or l2 or carry != 0:
            # 计算当前值
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            # 计算当前值 & 是否进位
            current_val = val % 10
            carry = val // 10

            # 创建下一个节点
            current.next = ListNode(current_val)
            current = current.next

            # 移动下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

    def get_length(self, l: Optional[ListNode]) -> int:
        len = 0
        while l:
            len += 1
            l = l.next
        return len

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # self.m1()
        # self.m2()
        #  方法三
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 获取长短链表
        len1 = self.get_length(l1)
        len2 = self.get_length(l2)
        if len1 >= len2:
            longer = l1
            shorter = l2
        else:
            shorter = l1
            longer = l2
        res = longer  # 结果，也就是长链表的头
        carry = 0  # 是否进位
        last_node = None  # 上一个节点
        # 遍历短链表
        while shorter:
            val = longer.val + shorter.val + carry
            longer.val = val % 10
            carry = val // 10
            last_node = longer
            longer = longer.next
            shorter = shorter.next

        while longer:
            val = longer.val + carry
            longer.val = val % 10
            carry = val // 10
            last_node = longer
            longer = longer.next

        if carry != 0:
            last_node.next = ListNode(carry)
        return res


if __name__ == '__main__':
    solution = Solution()

    # l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l2 = ListNode(5, ListNode(6, ListNode(4)))

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6))

    # l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l2 = ListNode(9)

    res = solution.addTwoNumbers(l1, l2)

    while res:
        print(res.val)
        res = res.next
