class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        tmp = head.val
        current = head

        while current.next is not None:
            # print("current:", current.val, "next:", current.next.val)
            if current.next.val == tmp:
                # print("skip")
                current.next = current.next.next
            else:
                current = current.next
                tmp = current.val

        return head


if __name__ == "__main__":
    nums = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3]
    head = ListNode(nums[0])
    current = head
    for x in nums[1:]:
        current.next = ListNode(x)
        current = current.next

    actual = Solution().deleteDuplicates(head)

    while actual is not None:
        print(actual.val, end="->")
        actual = actual.next
