from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calc(i, j):
            if dp[i][j] or j == i + 1:
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):
                coins = max(coins, nums[i] * nums[k] *
                            nums[j] + calc(i, k) + calc(k, j))
            dp[i][j] = coins
            return coins

        return calc(0, n - 1)
