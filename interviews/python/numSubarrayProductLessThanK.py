class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        start, product, count = 0, 1, 0
        for end in range(len(nums)):
            while start <= end and product * nums[end] >= k:
                product = product / nums[start]
                start += 1

            product = 1 if start > end else product * nums[end]
            count = count if start > end else count + (end - start + 1)

        return count
