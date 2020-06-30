class Solution:
    def romanToInt(self, s: str) -> int:
        before = ""
        res = 0
        letters = dict(
            I=(1, 5),
            V=(5, float("inf")),
            X=(10, 50),
            L=(50, float("inf")),
            C=(100, 500),
            D=(500, float("inf")),
            M=(1000, float("inf")),
        )

        for c in reversed(s):
            for letter, (v, threshold) in letters.items():
                if c == letter:
                    res += v if res < threshold else -v

        return res
