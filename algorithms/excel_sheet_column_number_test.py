import unittest
from .excel_sheet_column_number import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.titleToNumber('A'), 1)

    def test_example2(self):
        self.assertEqual(self.sol.titleToNumber('AB'), 28)

    def test_example3(self):
        self.assertEqual(self.sol.titleToNumber('ZY'), 701)
