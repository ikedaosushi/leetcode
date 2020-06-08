class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            minus = -1
            x = x * -1
        else:
            minus = 1

        x = int("".join(reversed(str(x))))
        if 2 ** 31 <= x:
            return 0
        return x * minus
