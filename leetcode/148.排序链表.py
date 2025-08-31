"""
148. 排序链表
https://leetcode.cn/problems/sort-list/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用数组承接，然后排序数组，最后组装链表
        if head is None or head.next is None:
            return head
        nodes, node = [], head
        while node:
            nodes.append(node)
            node = node.next
        nodes.sort(key=lambda x: x.val)
        new_head, prev = nodes[0], nodes[0]
        for i in range(1, len(nodes)):
            prev.next = nodes[i]
            prev = nodes[i]
        prev.next = None
        return new_head


if __name__ == '__main__':
    solution = Solution()

    linked = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    linked = solution.sortList(linked)

    while linked:
        print(linked.val)
        linked = linked.next
