from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        for n in nums:
            hs[n] += 1

        res = sorted(hs, key=hs.get, reverse=True)

        return res[:k]
