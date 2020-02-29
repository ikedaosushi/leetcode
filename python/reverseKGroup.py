class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None

        current = head
        count = 0

        while current and count < k:
            current = current.next
            count += 1

        if count < k:
            return head

        current = self.reverseKGroup(current, k)
        while count > 0:
            tmp = head.next
            head.next = current
            current = head
            head = tmp
            count -= 1

        return current


if __name__ == "__main__":
    nums, k = [1, 2, 3, 4, 5], 2
    current = root = ListNode(nums[0])
    for n in nums[1:]:
        current.next = ListNode(n)
        current = current.next

    actual = Solution().reverseKGroup(root, k)
    while actual:
        print(actual.val)
        actual = actual.next
