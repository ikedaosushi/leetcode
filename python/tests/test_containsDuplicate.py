import pytest
from containsDuplicate import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
])
def test_containsDuplicate(nums, expected):
    actual = Solution().containsDuplicate(nums)
    assert actual == expected
