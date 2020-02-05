import pytest
from isPalindrome import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


@pytest.mark.parametrize("nums,expected", [
    ([], True),
    ([1], True),
    ([1, 2], False),
    ([1, 2, 1], True),
    ([1, 2, 2, 1], True),
    ([1, 2, 3, 2, 1], True),
    ([1, 2, 3, 1], False),

])
def test_isPalindrome(nums, expected):
    if not nums:
        assert Solution().isPalindrome(None)
        return

    current = head = ListNode(nums[0])
    for n in nums[1:]:
        current.next = ListNode(n)
        current = current.next

    actual = Solution().isPalindrome(head)
    assert actual == expected
