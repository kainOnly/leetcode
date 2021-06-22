from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while n >= 0:
            digits[n] += 1
            digits[n] %= 10
            if digits[n] != 0:
                return digits
            n -= 1
        return [1] + digits
