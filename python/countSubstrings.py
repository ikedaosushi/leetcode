class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        dp = [
            [True if i == j else False for j in range(size)]
            for i in range(size)
        ]
        res = len(s)
        for j in range(1, size):
            for i in range(0, j):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i+1][j-1])
                print(f"i: {i}, j: {j}, dp[i][j]: {dp[i][j]}")
                res += dp[i][j]

        return res
