from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        counter = Counter(nums1)
        for n in nums2:
            if n in counter and counter[n] > 0:
                res.append(n)
                counter[n] -= 1

        return res
