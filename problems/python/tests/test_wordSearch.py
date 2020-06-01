import pytest
from wordSearch import Solution

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]


@pytest.mark.parametrize("word,expected", [
    ("ABCCED", True),
    ("SEE", True),
    ("ABCB", False)
])
def test_wordSearch(word, expected):
    actual = Solution().exist(board, word)
    assert actual == expected
