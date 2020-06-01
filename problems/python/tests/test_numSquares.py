import pytest
from numSquares import Solution


@pytest.mark.parametrize("n,expected", [
    (12, 3),
    (13, 2),
])
def test_numSquares(n, expected):
    actual = Solution().numSquares(n)
    assert actual == expected
