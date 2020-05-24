import pytest
from checkValidString import Solution


@pytest.mark.parametrize("s, expected", [
    ("()", True), ("(*)", True), ("(*))",
                                  True), (")()", False), ("", True), ("(()", False),
    ("(())((())()()(*)(*()(())())())()()((()())((()))(*", False)
])
def test_checkValidString(s, expected):
    actual = Solution().checkValidString(s)
    assert actual == expected
