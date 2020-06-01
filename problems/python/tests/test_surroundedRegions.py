import pytest
from surroundedRegions import Solution


@pytest.mark.parametrize("board, expected", [
    ([], []),
    (
        [["X", "X", "X", "X"], ["X", "O", "O", "X"], [
            "X", "X", "O", "X"], ["X", "O", "X", "X"]],
        [["X", "X", "X", "X"], ["X", "X", "X", "X"], [
            "X", "X", "X", "X"], ["X", "O", "X", "X"]]
    )
])
def test_surroundedRegions(board, expected):
    Solution().solve(board)
    assert board == expected
