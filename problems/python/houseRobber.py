from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return max(self._rob(nums, 0), self._rob(nums, 1))

    def _rob(self, nums: List[int], i: int):
        if len(nums) - i <= 0:
            return 0
        if i in self.memo:
            return self.memo[i]

        result = max(nums[i] + self._rob(nums, i + 2), self._rob(nums, i + 1))
        self.memo[i] = result

        return result
