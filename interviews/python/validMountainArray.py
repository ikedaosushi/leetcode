from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        last = len(A) - 1
        i = 0
        while i < last and A[i] < A[i+1]:
            i += 1

        if i in [0, last]:
            return False

        while i < last and A[i] > A[i+1]:
            i += 1

        return i == last
