import pytest
from fizzBuzz import Solution


@pytest.mark.parametrize("n, expected", [
    (0, []),
    (1, ["1"]),
    (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
          "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
])
def test_fizzBuzz(n, expected):
    actual = Solution().fizzBuzz(n)
    assert actual == expected
