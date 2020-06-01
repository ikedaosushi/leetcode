# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            c = b.next
            pre.next, a.next, b.next = b, c, a
            pre = a
        
        return dummy.next