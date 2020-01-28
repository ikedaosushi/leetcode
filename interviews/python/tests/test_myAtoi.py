import pytest
from myAtoi import Solution


@pytest.mark.parametrize("str, expected", [
    ("42", 42),
    ("+1", 1),
    ("         -42", -42),
    ("   +0 123", 0),
    ("   0 123", 0),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("2147483648", 2147483647),
    ("0-1", 0)
])
def test_myAtoi(str, expected):
    actual = Solution().myAtoi(str)
    assert actual == expected
