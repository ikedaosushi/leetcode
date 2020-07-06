from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        start, end = 0, len(A) - 1
        ans = []
        i = end
        while 0 <= i:
            pow1, pow2 = A[start] * A[start], A[end] * A[end]
            if pow1 > pow2:
                ans.insert(0, pow1)
                start += 1
            else:
                ans.insert(0, pow2)
                end -= 1
            i -= 1

        return ans
