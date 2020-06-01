import pytest
from removeDuplicates import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ([], 0)
])
def test_removeDuplicates(nums, expected):
    actual = Solution().removeDuplicates(nums)
    assert actual == expected
