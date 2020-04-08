import pytest
from generate import Solution


@pytest.mark.parametrize("numRows, expected", [
    (5, [
     [1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1],
     [1, 4, 6, 4, 1]
     ]),
    (0, []),
    (1, [[1]])
])
def test_generate(numRows, expected):
    actual = Solution().generate(numRows)
    assert actual == expected
