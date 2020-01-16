import pytest
from removeDuplicates import Solution


@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 2, 3], [1, 2, 2, 3]),
    ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
    ([1, 1, 1, 2, 2, 3, 3, 3, 3], [1, 1, 2, 2, 3, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3])
])
def test_removeDuplicates(nums, expected):
    length = Solution().removeDuplicates(nums)
    assert nums == expected
    assert len(nums) == length
