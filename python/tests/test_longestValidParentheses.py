import pytest
from longestValidParentheses import Solution


@pytest.mark.parametrize("s, expected", [
    ("(()", 2),
    (")()())", 4)
])
def test_longestValidParentheses(s, expected):
    actual = Solution().longestValidParentheses(s)
    assert actual == expected
