from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climb(n)

    @lru_cache()
    def _climb(self, n: int) -> int:
        if n < 2:
            return 1

        return self._climb(n - 1) + self._climb(n - 2)
