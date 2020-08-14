class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_ = set()
        for c in s:
            if c not in hash_:
                hash_.add(c)
            else:
                hash_.remove(c)

        return len(s) - len(hash_) + 1 if len(hash_) else len(s)
