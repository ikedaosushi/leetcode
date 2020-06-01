class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count("*") > length:
            return False

        dp = [True] + [False] * length

        for i in p:
            if i == "*":
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            else:
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == "?")

            dp[0] = dp[0] and i == "*"

        return dp[-1]
