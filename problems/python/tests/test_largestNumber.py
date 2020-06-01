import pytest
from largestNumber import Solution


@pytest.mark.parametrize("nums, expected", [
    ([0, 0], "0"),
    ([10, 2], "210"),
    ([3, 30, 34, 5, 9], "9534330")
])
def test_largestNumber(nums, expected):
    actual = Solution().largestNumber(nums)
    assert actual == expected
