from typing import List
from heapq import heappush, heappop


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if all(node is None for node in lists):
            return

        heap = []
        current = root = ListNode(None)

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        while heap:
            _, i, current.next = heappop(heap)
            current = current.next
            if current.next:
                heappush(heap, (current.next.val, i, current.next))

        return root.next


if __name__ == "__main__":
    nums_lists, expected = ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])

    lists = []
    for nums in nums_lists:
        current = root = ListNode(nums[0])
        for n in nums[1:]:
            current.next = ListNode(n)
            current = current.next
        lists.append(root)

    actual = Solution().mergeKLists(lists)
    current = actual
    # while current:
    #     print(current.val)
    #     current = current.next

    idx = 0
    while actual:
        assert actual.val == expected[idx]
        actual = actual.next
        idx += 1
