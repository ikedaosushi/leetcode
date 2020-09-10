class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = sum(s == g for s, g in zip(secret, guess))
        b = sum((Counter(secret) & Counter(guess)).values()) - a
        return f"{a}A{b}B"
