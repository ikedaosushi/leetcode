import pytest
from rangeBitwiseAnd import Solution


@pytest.mark.parametrize("m, n, expected", [
    (5, 7, 4),
    (0, 1, 0)
])
def test_rangeBitwiseAnd(m, n, expected):
    actual = Solution().rangeBitwiseAnd(m, n)
    assert actual == expected
