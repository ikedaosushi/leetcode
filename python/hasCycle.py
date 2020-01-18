# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        res = False
        current = head
        while current:
            if current.val is None:
                res = True
                break
            # print("current:", current.val)
            current.val = None

            current = current.next

        return res


if __name__ == "__main__":
    nums, pos, expected = ([3, 2, 0, -4], 1, True)
    nums, pos, expected = [1, 2], 0, True

    head = ListNode(nums[0])
    current = head
    idx = 0
    tail = None
    for x in nums[1:]:
        current.next = ListNode(x)
        if idx == pos:
            tail = current
        current = current.next
        idx += 1
    current.next = tail

    actual = Solution().hasCycle(head)
    print("actual:", actual)
