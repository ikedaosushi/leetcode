import pytest
from minDistance import Solution


@pytest.mark.parametrize("word1, word2, expected", [
    ("horse", "ros", 3),
    ("intention", "execution", 5)
])
def test_minDistance(word1, word2, expected):
    actual = Solution().minDistance(word1, word2)
    assert actual == expected
