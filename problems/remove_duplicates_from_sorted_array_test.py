import unittest
from .remove_duplicates_from_sorted_array import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.removeDuplicates([1, 1, 2]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
