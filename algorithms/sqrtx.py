class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        n, m = 1, x // 2
        while n < m:
            k = n + (m - n + 1) // 2
            if k > x // k:
                m = k - 1
            else:
                n = k
        return n
