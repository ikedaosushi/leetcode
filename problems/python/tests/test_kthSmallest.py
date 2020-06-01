import pytest
from kthSmallest import Solution


@pytest.mark.parametrize("matrix, k, expected", [
    ([
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ], 8, 13)
])
def test_kthSmallest(matrix, k, expected):
    actual = Solution().kthSmallest(matrix, k)
    assert actual == expected
