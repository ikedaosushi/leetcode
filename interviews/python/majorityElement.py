from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        c1, c2, can1, can2 = 0, 0, 0, 1
        for n in nums:
            if n == can1:
                c1 += 1
            elif n == can2:
                c2 += 1
            elif c1 == 0:
                can1, c1 = n, 1
            elif c2 == 0:
                can2, c2 = n, 1
            else:
                c1, c2 = c1 - 1, c2 - 1

        return [n for n in (can1, can2) if nums.count(n) > len(nums) // 3]
