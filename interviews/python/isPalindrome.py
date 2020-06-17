# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        last = None

        while fast and fast.next and fast.next.next:
            tmp = slow.next
            slow.next = last
            last = slow
            slow = tmp
            fast = fast.next.next

        while last or slow:
            if last.val != slow.val:
                return False
            else:
                last = last.next
                slow = slow.next

        return last is None and slow is None
