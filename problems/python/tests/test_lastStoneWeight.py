import pytest
from lastStoneWeight import Solution


@pytest.mark.parametrize("stones, expected", [
    ([2, 7, 4, 1, 8, 1], 1)
])
def test_lastStoneWeight(stones, expected):
    actual = Solution().lastStoneWeight(stones)
    assert actual == expected
