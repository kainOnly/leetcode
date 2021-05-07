class Solution:
    def reverse(self, x: int) -> int:
        Int32Min, Int32Max = -2147483648, 2147483647
        if x == 0 or x < Int32Min or x > Int32Max:
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
        if val < Int32Min or val > Int32Max:
            return 0
        return int(val)
