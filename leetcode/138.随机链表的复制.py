"""
138. 随机链表的复制
https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-100-liked
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        # 先在原链表复制新链表
        cur: Node = head
        while cur:
            new_node = Node(cur.val)  # 新节点
            tmp = cur.next
            cur.next = new_node
            new_node.next = tmp
            cur = tmp
        # 后在新增节点后的链表 操作random 指针
        cur: Node = head
        while cur:
            if cur.random:
                # 当前新节点的random节点
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 组装新链表
        node = head.next
        while node and node.next:
            node.next = node.next.next
            node = node.next

        return head.next
