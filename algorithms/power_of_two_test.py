import unittest
from .power_of_two import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.isPowerOfTwo(1), True)

    def test_example2(self):
        self.assertEqual(self.sol.isPowerOfTwo(2), True)

    def test_example3(self):
        self.assertEqual(self.sol.isPowerOfTwo(3), False)
