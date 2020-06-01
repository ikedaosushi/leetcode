import pytest
from firstMissingPositive import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([2, 2], 1),
    ([0, 3], 1)
])
def test_firstMissingPositive(nums, expected):
    actual = Solution().firstMissingPositive(nums)
    assert actual == expected
