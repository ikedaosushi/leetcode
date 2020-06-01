import pytest
from searchMatrix import Solution


@pytest.mark.parametrize("matrix,target,expected", [
    (
        [[]], 1, False
    ),
    (
        [[1]], 1, True
    ),
    (
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5, True
    ),
    (
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 20, False
    ),
    (
        [[0, 0, 0], [2, 7, 9], [7, 8, 11]],
        7, True
    )
])
def test_searchMatrix(matrix, target, expected):
    actual = Solution().searchMatrix(matrix, target)
    assert actual == expected
