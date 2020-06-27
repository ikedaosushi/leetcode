from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = res = nums[0]
        for i in range(1, len(nums)):
            tmp = dp[i-1] if dp[i-1] > 0 else 0
            dp[i] = nums[i] + tmp
            res = max(res, dp[i])

        return res
