from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        out = ""
        for p in permutations(A):
            if p[0] * 10 + p[1] <= 23 and p[2] <= 5:
                out = max(out, f"{p[0]}{p[1]}:{p[2]}{p[3]}")

        return out
