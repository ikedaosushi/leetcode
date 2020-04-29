import pytest
from maxPoints import Solution


@pytest.mark.parametrize("points, expected", [
    ([[1, 1], [2, 2], [3, 3]], 3),
    ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4)
])
def test_maxPoints(points, expected):
    actual = Solution().maxPoints(points)
    assert actual == expected
