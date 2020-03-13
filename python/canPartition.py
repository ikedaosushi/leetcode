from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half = int(sum(nums) / 2)

        dp = [True] + [False] * half

        for n in nums:
            for i in range(half, 0, -1):
                if i >= n:
                    # print("i:", i, " n:", n, " dp[i]:", dp[i], " dp[i -n]:", dp[i - n])
                    dp[i] = dp[i] or dp[i - n]
        print(dp)

        return dp[-1]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    Solution().canPartition(nums)
