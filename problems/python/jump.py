from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        ans = 1
        l, r = 0, nums[0]

        while r < len(nums) - 1:
            ans += 1
            next_ = max(i + nums[i] for i in range(l + 1, r + 1))
            l, r = r, next_

        return ans
