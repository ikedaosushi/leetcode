import pytest
from setZeroes import Solution


@pytest.mark.parametrize("matrix,expected", [
    (
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ],
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
    ),
    (
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ],
        [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
    ),
    (
        [
            [1, 1, 1],
            [0, 1, 2]
        ],
        [
            [0, 1, 1],
            [0, 0, 0]
        ]
    ),
    (
        [[1, 0, 3]],
        [[0, 0, 0]]
    ),
])
def test_setZeros(matrix, expected):
    Solution().setZeroes(matrix)
    assert matrix == expected
