import pytest
from climbStairs import Solution


@pytest.mark.parametrize("n,expected", [(2, 2), (3, 3), (1, 1), (4, 5)])
def test_climbStairs(n, expected):
    actual = Solution().climbStairs(n)
    assert actual == expected
