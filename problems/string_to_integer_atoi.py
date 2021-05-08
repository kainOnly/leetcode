class Solution:
    def myAtoi(self, s: str) -> int:
        Int32Min, Int32Max = -2147483648, 2147483647
        val, sign = 0, 1
        for char in s:
            if char == ' ' or char == '+':
                continue
            if char == '-':
                sign = -sign
                continue
            if char.isnumeric():
                n = int(char)
                val *= 10
                val += n * sign
                if val < Int32Min:
                    val = Int32Min
                    break
                if val > Int32Max:
                    val = Int32Max
                    break
            else:
                break
        return val
