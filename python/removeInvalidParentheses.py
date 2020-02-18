from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return []


if __name__ == "__main__":
    string, expected = "()())()", ["()()()", "(())()"]
    actual = Solution().removeInvalidParentheses(string)
    print(actual)
