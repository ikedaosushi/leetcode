import pytest
from findPeakElement import Solution


@pytest.mark.parametrize("nums, expected", [
    ([], [0]),
    ([1], [0]),
    ([1, 2], [1]),
    ([1, 2, 3, 1], [2]),
    ([1, 2, 1, 3, 5, 6, 4], [1, 5])
])
def test_findPeakElement(nums, expected):
    actual = Solution().findPeakElement(nums)
    assert actual in expected
