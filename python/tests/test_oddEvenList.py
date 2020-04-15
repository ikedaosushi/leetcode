import pytest
from oddEvenList import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
])
def test_oddEvenList(nums, expected):
    head = current = ListNode(nums[0])
    for n in nums[1:]:
        current.next = ListNode(n)
        current = current.next

    actual = Solution().oddEvenList(head)
    index = 0
    while actual:
        assert actual.val == expected[index]
        actual = actual.next
        index += 1
