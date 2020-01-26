from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_ = dict()
        threshold = len(nums) / 2
        for n in nums:
            if n in hash_:
                hash_[n] += 1
            else:
                hash_[n] = 1
            if hash_[n] > threshold:
                return n
