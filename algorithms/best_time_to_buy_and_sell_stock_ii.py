from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            income = prices[i] - prices[i - 1]
            if income > 0:
                profit += income
        return profit
