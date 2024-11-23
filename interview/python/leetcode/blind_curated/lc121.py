# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minUntilNow, profit = float('inf'), 0

        for p in prices:
            profit = max(profit, p-minUntilNow)
            minUntilNow = min(minUntilNow, p)

        return profit
