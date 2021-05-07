class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        signed = x < 0
        if signed:
            x = -x
        val = 0
        p = 10 ** (len(str(x)) - 1)
        while x != 0:
            n = x % 10
            val += p * n
            x //= 10
            p /= 10
        if signed:
            val = -val
        return int(val)
