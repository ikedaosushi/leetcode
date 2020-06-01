import pytest
from getSum import Solution


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-2, 3, 1)
])
def test_getSum(a, b, expected):
    actual = Solution().getSum(a, b)
    assert actual == expected
