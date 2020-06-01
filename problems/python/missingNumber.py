from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(1, 1 + len(nums))) - sum(nums)
