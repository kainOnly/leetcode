import unittest
from .search_insert_position import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.searchInsert([1, 3, 5, 6], 5), 2)

    def test_example2(self):
        self.assertEqual(self.sol.searchInsert([1, 3, 5, 6], 2), 1)

    def test_example3(self):
        self.assertEqual(self.sol.searchInsert([1, 3, 5, 6], 7), 4)

    def test_example4(self):
        self.assertEqual(self.sol.searchInsert([1, 3, 5, 6], 0), 0)
