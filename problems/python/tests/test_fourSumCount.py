import pytest
from fourSumCount import Solution


@pytest.mark.parametrize("A, B, C, D, expected", [
    ([1, 2], [-2, -1], [-1, 2], [0, 2], 2)
])
def test_fourSumCount(A, B, C, D, expected):
    actual = Solution().fourSumCount(A, B, C, D)
    assert actual == expected
