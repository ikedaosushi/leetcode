class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        dp = [0] * len(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    left = stack.pop()
                    dp[i] = dp[left - 1] + i - left + 1

        return max(dp)
