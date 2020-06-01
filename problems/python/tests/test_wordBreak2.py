import pytest
from wordBreak2 import Solution


@pytest.mark.parametrize("s, wordDict, expected", [
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"], [
        "cats and dog",
        "cat sand dog"
    ]), ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"], [
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"
    ])
])
def test_wordcreak(s, wordDict, expected):
    actual = Solution().wordBreak(s, wordDict)
    assert set(actual) == set(expected)
