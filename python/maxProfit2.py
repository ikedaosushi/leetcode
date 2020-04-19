from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for idx in range(len(prices)-1):
            if prices[idx+1] > prices[idx]:
                total += prices[idx+1] - prices[idx]

        return total
