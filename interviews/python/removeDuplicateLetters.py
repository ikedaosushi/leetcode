class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ""))
        return ""
