"""
146. LRU 缓存
https://leetcode.cn/problems/lru-cache/description/?envType=study-plan-v2&envId=top-100-liked
"""
from typing import Optional


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache: list[tuple[int, int]] = []  # [<key,value>, ...]
#
#     def get(self, key: int) -> int:
#         index = -1
#         # 查找
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 index = i
#         if index == -1:
#             return -1
#         value = self.cache[index][1]
#         # 重排
#         self.cache.insert(0, self.cache.pop(index))
#         return value
#
#     def put(self, key: int, value: int) -> None:
#         # 查找，判断是否存在
#         index = -1
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 index = i
#         if index != -1:  # 存在，那么更新值，然后重排
#             self.cache[index] = (key, value)
#             self.cache.insert(0, self.cache.pop(index))
#         else:  # 不存在
#             if len(self.cache) >= self.capacity:  # 如果从超过容量，则淘汰最后一个
#                 self.cache.pop(len(self.cache) - 1)
#             # 添加即可
#             self.cache.insert(0, (key, value))

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev: Optional['DLinkedNode'] = None
        self.next: Optional['DLinkedNode'] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLinkedNode()  # 哑节点
        self.tail = DLinkedNode()  # 哑节点
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        self.node_cache: dict[int, DLinkedNode] = {}

    def add_to_head(self, node: DLinkedNode):
        """ 将新节点放入到链表的头节点中 """
        self.node_cache[node.key] = node
        self.count += 1
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node: DLinkedNode):
        if node.key not in self.node_cache:  # 不在就没必要 remove 了
            return
        self.count -= 1
        self.node_cache.pop(node.key)
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node: DLinkedNode):
        """ 将当前链表中某节点移动到最前 """
        self.remove_node(node)
        self.add_to_head(node)

    def get(self, key: int) -> int:
        if key in self.node_cache:
            value = self.node_cache[key].value
            # 当前节点移到头部
            self.move_to_head(self.node_cache[key])
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        node = self.node_cache.get(key)
        if node:  # 存在，更新后 重拍（当前节点放最前）
            node.value = value
            self.move_to_head(node)
        else:  # 不存在，那么需要判断 是否超过限制
            node = DLinkedNode(key, value)
            # 超过了，那么需要移除尾部节点
            if self.count >= self.capacity:
                self.remove_node(self.tail.prev)
            # 不管超没好过，都将新节点，添加到链表中
            self.add_to_head(node)


if __name__ == '__main__':
    lru_cache = LRUCache(2)

    # lru_cache.put(2, 1)
    # lru_cache.put(2, 2)
    # print(lru_cache.get(2))
    # lru_cache.put(1, 1)
    # lru_cache.put(4, 1)
    # print(lru_cache.get(2))

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))
    lru_cache.put(3, 3)
    print(lru_cache.get(2))
    lru_cache.put(4, 4)
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
