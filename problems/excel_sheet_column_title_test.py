import unittest
from .excel_sheet_column_title import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.convertToTitle(1), 'A')

    def test_example2(self):
        self.assertEqual(self.sol.convertToTitle(28), 'AB')
