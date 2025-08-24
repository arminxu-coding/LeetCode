"""
25. K 个一组翻转链表
https://leetcode.cn/problems/reverse-nodes-in-k-group/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, left: ListNode, right: ListNode) -> tuple[ListNode, ListNode]:
        """  从 left 到 right 反转链表 """
        node, prev = left, None
        while prev != right:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return right, left

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        prev = head = ListNode(0, left)
        while True:
            i, right = 1, left
            while i < k and right:
                i += 1
                right = right.next

            if right is None:
                break

            next_node = right.next
            # 反转链表
            left, right = self.reverse_list(left, right)
            prev.next = left
            left = right.next = next_node
            prev = right

        return head.next


if __name__ == '__main__':
    solution = Solution()
    node = solution.reverseKGroup(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        2
    )

    # right = ListNode(5)
    # left = ListNode(1, ListNode(2, ListNode(3, ListNode(4, right))))
    # node, right = solution.reverse_list(left, right)

    while node:
        print(node.val)
        node = node.next
