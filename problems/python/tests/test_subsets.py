import unittest

import pytest
from subsets import Solution

case = unittest.TestCase()


@pytest.mark.parametrize("nums,expected", [
    (
        [1, 2],
        [
            [1],
            [2],
            [1, 2],
            []
        ]
    ),
    (
        [1, 2, 3],
        [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]
    ),
    (
        [1, 2, 3, 4],
        [
            [],
            [1],
            [2],
            [3],
            [4],
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [3, 4],
            [1, 2, 3],
            [1, 2, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4]
        ]
    ),
])
def test_subsets(nums, expected):
    actual = Solution().subsets(nums)
    case.assertCountEqual(actual, expected)
