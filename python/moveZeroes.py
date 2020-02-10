from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        n = len(nums)
        while idx < n:
            if nums[idx] == 0:
                nums.append(nums.pop(idx))
                n -= 1
            else:
                idx += 1
