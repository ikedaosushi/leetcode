from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        dp = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - coin] if i - coin >= 0 else MAX for coin in coins) + 1

        return [dp[-1], -1][dp[-1] == MAX]
