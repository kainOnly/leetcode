import unittest
from .reverse_integer import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.reverse(123), 321)

    def test_example2(self):
        self.assertEqual(self.sol.reverse(-123), -321)

    def test_example3(self):
        self.assertEqual(self.sol.reverse(120), 21)

    def test_example4(self):
        self.assertEqual(self.sol.reverse(0), 0)
