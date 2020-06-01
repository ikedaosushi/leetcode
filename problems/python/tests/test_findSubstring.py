import pytest
from findSubstring import Solution


@pytest.mark.parametrize("s, words, expected", [
    ("", [], []),
    ("a", [], []),
    ("a", [[], []], []),
    ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], [])
])
def test_findSubstring(s, words, expected):
    actual = Solution().findSubstring(s, words)
    assert actual == expected
