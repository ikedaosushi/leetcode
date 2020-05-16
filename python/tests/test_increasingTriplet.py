import pytest
from increasingTriplet import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    ([5, 1, 3, 6, 4], True)
])
def test_increasingTriplet(nums, expected):
    actual = Solution().increasingTriplet(nums)
    assert actual == expected
