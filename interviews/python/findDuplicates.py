from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        for i in range(n - 1):
            nums[(nums[i] % n) - 1] += n

        return [i + 1 for i in range(n - 1) if nums[i] > 2 * n]
