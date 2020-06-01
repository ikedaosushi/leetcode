from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        before = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == before:
                nums.pop(i)
            else:
                before = nums[i]
                i += 1

        return i
