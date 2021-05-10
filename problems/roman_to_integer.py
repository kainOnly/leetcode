class Solution:
    def romanToInt(self, s: str) -> int:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val, pre = 0, 0
        for key in s:
            n = num[key] if key in num else 0
            val += -pre if n > pre else pre
            pre = n
        val += pre
        return val
