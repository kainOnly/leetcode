class Solution:
    def myAtoi(self, s: str) -> int:
        Int32Min, Int32Max = -2147483648, 2147483647
        val, sign = 0, 0
        for char in s.strip():
            if sign == 0 and char.isspace():
                continue
            if sign == 0 and char == '+':
                sign = 1
                continue
            if sign == 0 and char == '-':
                sign = -1
                continue
            if char.isnumeric():
                if sign == 0:
                    sign = 1
                val *= 10
                val += int(char) * sign
                if val < Int32Min:
                    val = Int32Min
                    break
                if val > Int32Max:
                    val = Int32Max
                    break
            else:
                break
        return val
