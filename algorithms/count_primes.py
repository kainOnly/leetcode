class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n < 2:
            return count
        isPrimes = [True] * n
        for i in range(2, n):
            if isPrimes[i]:
                count += 1
                x = 2 * i
                while x < n:
                    isPrimes[x] = False
                    x += i
        return count
