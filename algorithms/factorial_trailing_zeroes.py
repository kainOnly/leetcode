class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero = 0
        while n > 0:
            n //= 5
            zero += n
        return zero
