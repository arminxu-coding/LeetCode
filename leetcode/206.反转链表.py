"""
206. 反转链表
https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev, cur = head, head.next
        prev.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


if __name__ == '__main__':
    solution = Solution()

    linked = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    linked = solution.reverseList(linked)

    while linked:
        print(linked.val)
        linked = linked.next
