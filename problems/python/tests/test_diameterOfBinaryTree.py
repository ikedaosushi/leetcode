import pytest
from diameterOfBinaryTree import Solution
from utils.binary_tree import from_nums


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 5], 3)
])
def test_diameterOfBinaryTree(nums, expected):
    actual = Solution().diameterOfBinaryTree(from_nums(nums))
    assert actual == expected
