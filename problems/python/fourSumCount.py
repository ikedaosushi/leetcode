from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = {}

        for c in C:
            for d in D:
                sum_ = c + d
                dic[sum_] = dic.get(sum_, 0) + 1

        res = 0
        for a in A:
            for b in B:
                res += dic.get(-1 * (a + b), 0)

        return res
