from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start, end = 0, len(A) - 1
        while start < end:
            while start < end:
                if A[start] % 2 == 0:
                    start += 1
                else:
                    break

            while start < end:
                if A[end] % 2 == 1:
                    end -= 1
                else:
                    break

            if start < end:
                A[start], A[end] = A[end], A[start]

        return A
