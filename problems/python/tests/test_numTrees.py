import pytest
from numTrees import Solution


@pytest.mark.parametrize("num, expected", [
    (3, 5),
    (4, 14),
    (5, 42)
])
def test_numTrees(num, expected):
    actual = Solution().numTrees(num)
    assert actual == expected
