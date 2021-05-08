import unittest
from .string_to_integer_atoi import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.myAtoi('42'), 42)

    def test_example2(self):
        self.assertEqual(self.sol.myAtoi('   -42'), -42)

    def test_example3(self):
        self.assertEqual(self.sol.myAtoi('4193 with words'), 4193)

    def test_example4(self):
        self.assertEqual(self.sol.myAtoi('words and 987'), 0)

    def test_example5(self):
        self.assertEqual(self.sol.myAtoi('-91283472332'), -2147483648)

    def test_example6(self):
        self.assertEqual(self.sol.myAtoi('+-12'), -12)
