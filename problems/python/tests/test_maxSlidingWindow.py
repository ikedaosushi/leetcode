import pytest
from maxSlidingWindow import Solution


@pytest.mark.parametrize("nums,k,expected", [
    ([], 1, []),
    ([], 3, []),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([9, 11], 2, [11]),
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),

])
def test_maxSlidingWindow(nums, k, expected):
    actual = Solution().maxSlidingWindow(nums, k)
    assert actual == expected
