class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        a = b = head
        dic = {}
        while a:
            dic[a] = Node(a.val)
            a = a.next
        while b:
            dic[b].next = dic.get(b.next)
            dic[b].random = dic.get(b.random)
            b = b.next

        return b.get(head)

        
        