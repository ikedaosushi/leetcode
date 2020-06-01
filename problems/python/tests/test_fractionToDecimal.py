import pytest
from fractionToDecimal import Solution


@pytest.mark.parametrize("numerator, denominator, expected", [
    (1, 2, "0.5"),
    (2, 1, "2"),
    (2, 3, "0.(6)")
])
def test_fractionToDecimal(numerator, denominator, expected):
    actual = Solution().fractionToDecimal(numerator, denominator)
    assert actual == expected
