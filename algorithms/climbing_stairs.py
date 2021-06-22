class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        f = [1, 2]
        for _ in range(n - 2):
            f.append(f[-1] + f[-2])
        return f[-1]
