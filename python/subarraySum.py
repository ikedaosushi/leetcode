from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        sum_ = 0
        res = 0

        for n in nums:
            sum_ += n
            if (sum_ - k) in dic:
                res += dic[sum_ - k]

            dic[sum_] += 1

        return res
