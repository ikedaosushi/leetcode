
class LinkedNode:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = LinkedNode(0, 0)
        self.tail = LinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, k):
        if k in self.dic:
            node = self.dic[k]
            self._remove(node)
            self._add(node)
            return node.v
        return -1

    def put(self, k, v):
        if k in self.dic:
            self._remove(self.dic[k])
        node = LinkedNode(k, v)
        self._add(node)
        if len(self.dic) > self.capacity:
            self._remove(self.tail.prev)

    def _add(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        self.dic[node.k] = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.dic[node.k]
