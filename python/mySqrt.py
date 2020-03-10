class Solution:
    def mySqrt(self, x: int) -> int:
        current = x
        while current ** 2 > x:
            current = int((current + x / current) / 2)
        return current

    def _mySqrt(self, x: int) -> int:
        idx = 0
        while True:
            if idx ** 2 > x:
                return idx - 1
            idx += 1
