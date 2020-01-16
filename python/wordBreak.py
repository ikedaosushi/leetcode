from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            # print("i:", i)
            # print("dp:", dp)
            if not dp[i]:
                continue
            for j in range(len(s)):
                # print("s[i:j + 1]:", s[i:j + 1])
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = True
                    # print("dp:", dp)

        return dp[-1]


if __name__ == "__main__":
    s, wordDict, expected = ("leetcode", ["leet", "code"], True)
    actual = Solution().wordBreak(s, wordDict)
    print(actual)
