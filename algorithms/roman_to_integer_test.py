import unittest
from .roman_to_integer import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.romanToInt('III'), 3)

    def test_example2(self):
        self.assertEqual(self.sol.romanToInt('IV'), 4)

    def test_example3(self):
        self.assertEqual(self.sol.romanToInt('IX'), 9)

    def test_example4(self):
        self.assertEqual(self.sol.romanToInt('LVIII'), 58)

    def test_example5(self):
        self.assertEqual(self.sol.romanToInt('MCMXCIV'), 1994)
