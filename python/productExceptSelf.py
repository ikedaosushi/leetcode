from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = 1
        output = []
        for i in range(n):
            output.append(c)
            c = c * nums[i]

        c = 1
        for i in range(n):
            j = n - i - 1
            output[j] = output[j] * c
            c = c * nums[j]

        return output
