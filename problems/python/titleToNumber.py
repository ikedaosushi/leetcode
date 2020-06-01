class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = 0
        for i, c in enumerate(reversed(s)):
            res += (alphabet.index(c) + 1) * (26 ** i)

        return res
