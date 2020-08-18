from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        cur = range(10)
        for i in range(N - 1):
            cur = set(
                x*10 + y for x in cur
                for y in [x % 10 + K, x % 10 - K]
                if x and 0 <= y < 10
            )
        return list(cur)
