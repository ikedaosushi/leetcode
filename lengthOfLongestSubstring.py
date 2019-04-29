class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_ls = [x for x in s]

        max_len = 0
        substring = []
        for a in a_ls:
            if a in substring:
                idx = substring.index(a)
                substring = substring[idx + 1:]
            substring.append(a)
            if max_len < len(substring):
                max_len = len(substring)

        return max_len