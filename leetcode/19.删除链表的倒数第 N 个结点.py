"""
19. 删除链表的倒数第 N 个结点
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 数组承接，保存中间态
        # if head is None:
        #     return head
        # length = 0
        # node = head
        # nodes = []
        # while node:
        #     length += 1
        #     nodes.append(node)
        #     node = node.next
        #
        # if n == length:
        #     return head.next
        # nodes[length - n - 1].next = nodes[length - n - 1].next.next
        # return head

        # 栈
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        prev = None
        index = 0
        while len(nodes) > 0:
            index += 1
            cur = nodes.pop()
            if index == n:
                continue
            cur.next = prev
            prev = cur
        return prev


if __name__ == '__main__':
    solution = Solution()
    linked = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    node = solution.removeNthFromEnd(linked, 2)

    while node:
        print(node.val)
        node = node.next
