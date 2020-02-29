import pytest
from reverseKGroup import Solution, ListNode


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
])
def test_reverseKGroup(nums, k, expected):
    current = root = ListNode(nums[0])
    for n in nums[1:]:
        current.next = ListNode(n)
        current = current.next

    actual = Solution().reverseKGroup(root, k)
    idx = 0
    while actual:
        assert actual.val == expected[idx]
        actual = actual.next
        idx += 1
