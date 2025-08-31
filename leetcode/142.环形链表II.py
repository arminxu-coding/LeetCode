"""
142. 环形链表 II
https://leetcode.cn/problems/linked-list-cycle-ii/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                node = head
                while node != slow:
                    node = node.next
                    slow = slow.next
                return node
        return None


if __name__ == '__main__':
    solution = Solution()

    last = ListNode(5)
    node = ListNode(2, ListNode(3, ListNode(4, last)))
    last.next = node
    linked = ListNode(1, node)

    print(solution.detectCycle(linked).val)

    print(solution.hasCycle(linked))
