import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, lowest = 0, math.inf
        for price in prices:
            profit = max(price - lowest, profit)
            lowest = min(price, lowest)
        return profit
