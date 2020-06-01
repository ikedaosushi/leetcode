import pytest
from largestRectangleArea import Solution


@pytest.mark.parametrize("heights, expected", [
    ([2, 1, 5, 6, 2, 3], 10)
])
def test_largestRectangleArea(heights, expected):
    actual = Solution().largestRectangleArea(heights)
    assert actual == expected
