class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y, val = x, 0
        while y > 0:
            n = y % 10
            y //= 10
            val *= 10
            val += n

        return x == val
