from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        ans = [0] * size
        for n in nums:
            if 0 >= n or n > size:
                continue
            ans[n-1] = 1

        print(ans)
        for i, n in enumerate(ans):
            if n == 0:
                print(i)
                return i + 1

        return size + 1
