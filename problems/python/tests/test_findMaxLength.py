import pytest
from findMaxLength import Solution


@pytest.mark.parametrize("nums, expected", [
    ([0, 1], 2), ([0, 1, 0], 2),
    ([0, 1, 1, 0, 1, 1, 1, 0], 4)
])
def test_findMaxLength(nums, expected):
    actual = Solution().findMaxLength(nums)
    assert actual == expected
