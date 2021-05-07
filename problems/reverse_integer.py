class Solution:
    def reverse(self, x: int) -> int:
        def offset(n: int) -> bool:
            return n < -2147483648 or n > 2147483647

        if x == 0 or offset(x):
            return 0

        signed = x < 0
        if signed:
            x = -x

        val = 0
        while x != 0:
            val *= 10
            val += x % 10
            x //= 10

        if signed:
            val = -val

        return 0 if offset(val) else int(val)
