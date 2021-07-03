import unittest
from .count_primes import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.countPrimes(10), 4)

    def test_example2(self):
        self.assertEqual(self.sol.countPrimes(0), 0)

    def test_example3(self):
        self.assertEqual(self.sol.countPrimes(1), 0)
