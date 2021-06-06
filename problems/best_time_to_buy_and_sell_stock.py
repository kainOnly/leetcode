from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if prices[j] - prices[i] > num:
                    num = profit
        return num
