import unittest
from .factorial_trailing_zeroes import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.trailingZeroes(3), 0)

    def test_example2(self):
        self.assertEqual(self.sol.trailingZeroes(5), 1)

    def test_example3(self):
        self.assertEqual(self.sol.trailingZeroes(10), 2)
