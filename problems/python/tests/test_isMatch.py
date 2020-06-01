import pytest
from isMatch import Solution


@pytest.mark.parametrize("s, p, expected", [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False)
])
def test_isMatch(s, p, expected):
    actual = Solution().isMatch(s, p)
    assert actual == expected
