"""
234. 回文链表
https://leetcode.cn/problems/palindrome-linked-list/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = list()
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        node = head
        while node:
            if node.val != stack.pop():
                return False
            node = node.next
        return True
