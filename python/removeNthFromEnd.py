# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        length -= n
        # print(length)

        current = dummy
        while length > 0:
            length -= 1
            current = current.next
        current.next = current.next.next

        return dummy.next