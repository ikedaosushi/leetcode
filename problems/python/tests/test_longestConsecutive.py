import pytest
from longestConsecutive import Solution


@pytest.mark.parametrize("nums, expected", [
    ([100, 4, 200, 1, 3, 2], 4)
])
def test_longestConsecutive(nums, expected):
    actual = Solution().longestConsecutive(nums)
    assert actual == expected
