from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[-k]

    def quickSort(self, nums, start, end):
        if start < end:
            p = self.partition(nums, start, end)
            self.quickSort(nums, start, p - 1)
            self.quickSort(nums, p + 1, end)

    def partition(self, nums, start, end):
        pivot = nums[start]
        low = start + 1
        high = end

        while True:
            while low <= high and nums[low] <= pivot:
                low += 1
            while low <= high and pivot <= nums[high]:
                high -= 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
            else:
                break
        nums[start], nums[high] = nums[high], nums[start]
        return high
