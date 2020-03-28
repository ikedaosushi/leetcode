import pytest
from maxPathSum import Solution

from utils.binary_tree import from_nums


@pytest.mark.parametrize("nums, expected", [
    ([-3], -3),
    ([1], 1),
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48)
])
def test_maxPathSum(nums, expected):
    actual = Solution().maxPathSum(from_nums(nums))
    assert actual == expected
