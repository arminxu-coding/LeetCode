"""
21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/description/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一：遍历
        # if list1 is None and list2 is None:
        #     return None
        # elif list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        # if list1.val <= list2.val:
        #     head = node = list1
        #     list1 = list1.next
        # else:
        #     head = node = list2
        #     list2 = list2.next
        #
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         node.next = list1
        #         node = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         node = list2
        #         list2 = list2.next
        #
        # while list1:
        #     node.next = list1
        #     node = list1
        #     list1 = list1.next
        # while list2:
        #     node.next = list2
        #     node = list2
        #     list2 = list2.next
        # return head

        # 方法二：递归
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == '__main__':

    solution = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    node = solution.mergeTwoLists(l1, l2)

    while node:
        print(node.val)
        node = node.next
