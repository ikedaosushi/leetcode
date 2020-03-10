import pytest
from removeInvalidParentheses import Solution


@pytest.mark.parametrize("string,expected", [
    ("()())()", ["()()()", "(())()"]),
    ("()()))()", ["()()()", "(())()"]),
    ("(a)())()", ["(a)()()", "(a())()"]),
    (")(", [""]),
    ("", [""])
])
def test_removeInvalidParentheses(string, expected):
    actual = Solution().removeInvalidParentheses(string)
    assert set(actual) == set(expected)
