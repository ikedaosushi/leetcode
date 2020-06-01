import pytest
from findOrder import Solution


@pytest.mark.parametrize("n, p, expected", [
    (2, [[1, 0]], [0, 1]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3])
])
def test_findOrder(n, p, expected):
    actual = Solution().findOrder(n, p)
    assert set(actual) == set(expected)
