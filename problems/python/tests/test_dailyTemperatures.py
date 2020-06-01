import pytest
from dailyTemperatures import Solution


@pytest.mark.parametrize("T, expected", [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
])
def test_dailyTemperatures(T, expected):
    actual = Solution().dailyTemperatures(T)
    assert actual == expected
