import pytest
from addBinary import Solution


@pytest.mark.parametrize("a,b,expected", [
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
    ("0", "1", "1"),
    ("0", "0", "0"),
    ("1111111", "0", "1111111"),
    ("1111", "1111", "11110")
])
def test_addBinary(a, b, expected):
    actual = Solution().addBinary(a, b)
    assert actual == expected
