"""
23. 合并 K 个升序链表
https://leetcode.cn/problems/merge-k-sorted-lists/
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # index, length = 0, len(lists)
        # while index < length:
        #     if lists[index] is None:
        #         lists.pop(index)
        #         index -= 1
        #         length -= 1
        #     index += 1
        # if len(lists) == 0:
        #     return None
        #
        # def find_min() -> int:
        #     index, min_index, min_val = 0, 0, 10 ** 4
        #     while index < len(lists):
        #         if lists[index].val < min_val:
        #             min_index = index
        #             min_val = lists[index].val
        #         index += 1
        #     return min_index
        #
        # head = ListNode()
        # min_index = find_min()
        # head.next = lists[min_index]
        # lists[min_index] = lists[min_index].next
        # node = head.next
        # if lists[min_index] is None:
        #     lists.pop(min_index)
        #
        # length = len(lists)
        # while length > 0:
        #     min_index = find_min()
        #     node.next = lists[min_index]
        #     lists[min_index] = lists[min_index].next
        #     node = node.next
        #     if lists[min_index] is None:
        #         lists.pop(min_index)
        #         length -= 1
        # return head.next

        def merge_tow_list(l1: ListNode, l2: ListNode) -> ListNode:
            """ 合并两个链表 """
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            node = head = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 if l1 else l2
            return head.next

        length = len(lists)
        if length == 0:
            return None
        for i in range(1, length):
            lists[i] = merge_tow_list(lists[i - 1], lists[i])
        return lists[length - 1]


if __name__ == '__main__':
    solution = Solution()
    node = solution.mergeKLists([
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ])

    node = solution.mergeKLists([
        ListNode(1)
    ])

    node = solution.mergeKLists([
        None,
        None
    ])

    node = solution.mergeKLists([])

    while node:
        print(node.val)
        node = node.next
