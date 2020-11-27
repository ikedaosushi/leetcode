from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, n = sum(nums), len(nums)
        if target & 1:
            return False

        target >>= 1
        dp = [True] + [False] * target
        for x in nums:
            dp = [dp[s] or s >= x and dp[s - x] for s in range(target + 1)]
            if dp[target]:
                return True

        return False
