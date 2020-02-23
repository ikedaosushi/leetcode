import pytest
from regularExpressionMatching import Solution


@pytest.mark.parametrize("s, p, expected", [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False)
])
def test_regularExpressionMatching(s, p, expected):
    actual = Solution().isMatch(s, p)
    assert actual == expected
