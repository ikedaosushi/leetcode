import pytest
from pathSum import Solution
from utils.binary_tree import from_nums


@pytest.mark.parametrize("nums, sum_, expected", [
    ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
])
def test_pathSum(nums, sum_, expected):
    actual = Solution().pathSum(from_nums(nums), sum_)
    assert actual == expected
