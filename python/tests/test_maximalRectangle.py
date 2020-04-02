import pytest
from maximalRectangle import Solution


@pytest.mark.parametrize("matrix, expected", [
    ([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ], 6)
])
def test_maximalRectangle(matrix, expected):
    actual = Solution().maximalRectangle(matrix)
    assert actual == expected
