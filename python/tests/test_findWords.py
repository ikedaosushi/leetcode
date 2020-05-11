import pytest
from findWords import Solution


@pytest.mark.parametrize("board, words, expected", [
    ([
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ], ["oath", "pea", "eat", "rain"], ["eat", "oath"])
])
def test_findWords(board, words, expected):
    actual = Solution().findWords(board, words)
    assert sorted(actual) == sorted(expected)
