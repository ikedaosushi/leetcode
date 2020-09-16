class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = {n >> i for n in nums}
            ans += any(ans ^ 1 ^ p in prefixes for p in prefixes)
        return ans
