from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state machine
        hold, not_hold, cooldown = float("-inf"), 0, float("-1")
        for p in prices:
            hold, not_hold, cooldown = max(hold, not_hold - p), max(not_hold, cooldown), hold + p
            print("price:", p, "hold:", hold, "not_hold:", not_hold, "cooldown:", cooldown)
        return max(not_hold, cooldown)


if __name__ == "__main__":
    nums = [1, 2, 3, 0, 2]
    Solution().maxProfit(nums)
