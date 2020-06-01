class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {}
        return self._climb(n)

    def _climb(self, n: int) -> int:
        if n < 2:
            return 1
        cache = self.cache.get(n)
        if cache:
            return cache

        res = self._climb(n - 1) + self._climb(n - 2)
        self.cache[n] = res

        return res
