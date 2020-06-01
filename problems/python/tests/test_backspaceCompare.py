import pytest
from backspaceCompare import Solution


@pytest.mark.parametrize("s, t, expected", [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False)
])
def test_backspaceCompare(s, t, expected):
    actual = Solution().backspaceCompare(s, t)
    assert actual == expected
