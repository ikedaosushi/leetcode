import pytest
from twoSum import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2])
])
def test_twoSum(nums, target, expected):
    actual = Solution().twoSum(nums, target)
    assert set(actual) == set(expected)
