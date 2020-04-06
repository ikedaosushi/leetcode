from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        dic = {}
        for n in nums:
            if n not in dic:
                left = dic.get(n-1, 0)
                right = dic.get(n+1, 0)
                sum_ = left + right + 1
                res = max(res, sum_)
                dic[n] = sum_
                dic[n - left] = sum_
                dic[n + right] = sum_

        return res
