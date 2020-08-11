from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        len_ = len(citations)
        for i in range(len_):
            if citations[i] >= len_ - i:
                return len_ - i

        return 0
