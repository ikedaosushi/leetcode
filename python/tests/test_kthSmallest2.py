import pytest
from kthSmallest2 import Solution
from utils.binary_tree import from_nums


@pytest.mark.parametrize("nums, k, expected", [
    ([3, 1, 4, None, 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3)
])
def test_kthSmallest(nums, k, expected):
    actual = Solution().kthSmallest(from_nums(nums), k)
    assert actual == expected
