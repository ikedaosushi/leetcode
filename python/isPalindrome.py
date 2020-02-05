# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        if head is None:
            return True

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            current = slow
            slow = slow.next
            current.next = prev
            prev = current

        last = current

        while last:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next

        return True


if __name__ == "__main__":
    nums = [1, 2, 2, 1]
    current = head = ListNode(nums[0])
    for n in nums[1:]:
        current.next = ListNode(n)
        current = current.next

    actual = Solution().isPalindrome(head)
    print("actual:", actual)
