import pytest
from countPrimes import Solution


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (10, 4)
])
def test_countPrimes(n, expected):
    actual = Solution().countPrimes(n)
    assert actual == expected
