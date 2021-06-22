import unittest
from .sqrtx import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.mySqrt(4), 2)

    def test_example2(self):
        self.assertEqual(self.sol.mySqrt(8), 2)
