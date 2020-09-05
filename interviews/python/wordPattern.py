class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        t = str.split()
        return list(map(pattern.find, pattern)) == list(map(t.index, t))
