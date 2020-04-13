import pytest
from gameOfLife import Solution


@pytest.mark.parametrize("board, expected", [
    ([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ], [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ])
])
def test_gameOfLife(board, expected):
    Solution().gameOfLife(board)
    assert board == expected
