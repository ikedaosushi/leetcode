class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            current = nums[i] if nums[i] > 0 else -1 * nums[i]
            if nums[current - 1] > 0:
                nums[current - 1] *= -1

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
