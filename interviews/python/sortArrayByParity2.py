from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start, end = 0, len(A) - 1
        while start < end:
            while A[start] % 2 == 0 and start < end:
                start += 1
            while A[end] % 2 == 1 and start < end:
                end -= 1
            A[start], A[end] = A[end], A[start]

        return A
