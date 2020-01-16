import unittest

import pytest
from wordBreak import Solution

# s = "leetcode", wordDict = ["leet", "code"], true
# s = "applepenapple", wordDict = ["apple", "pen"], true
# s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"], false


@pytest.mark.parametrize("s,wordDict,expected", [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("aaaaaaa", ["aaaa", "aaa"], True)
])
def test_wordBreak(s, wordDict, expected):
    actual = Solution().wordBreak(s, wordDict)
    assert actual == expected
