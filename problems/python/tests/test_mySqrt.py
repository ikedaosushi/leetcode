import pytest
from mySqrt import Solution


@pytest.mark.parametrize("x, expected", [
    (4, 2), (8, 2)
])
def test_mySqrt(x, expected):
    actual = Solution().mySqrt(x)
    assert actual == expected
