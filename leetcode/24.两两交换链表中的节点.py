"""
24. 两两交换链表中的节点
https://leetcode.cn/problems/swap-nodes-in-pairs/description/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        l1 = head
        l2 = head.next
        head = l2
        prev = None
        while True:
            next = l2.next
            l2.next = l1
            l1.next = next
            if prev:
                prev.next = l2
            prev = l1
            if l1.next is None or l1.next.next is None:
                break
            l1 = l1.next
            l2 = l1.next
        return head

                                
if __name__ == '__main__':
    solution = Solution()
    node = solution.swapPairs(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    )
    while node:
        print(node.val)
        node = node.next
