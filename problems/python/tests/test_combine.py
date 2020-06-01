import pytest
import unittest
from combine import Solution
from itertools import combinations

case = unittest.TestCase()


@pytest.mark.parametrize("n,k", [(4, 2), (3, 2), (5, 2), (6, 3), (7, 4), (8, 5)])
def test_combine(n, k):
    actual = Solution().combine(n, k)
    expected = [list(node) for node in combinations(range(1, n + 1), k)]
    case.assertCountEqual(actual, expected)
