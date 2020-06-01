from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1

        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                if nums[i-1] < nums[i]:
                    return i
                i += 1

            i += 1
        return 0
