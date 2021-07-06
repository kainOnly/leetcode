import unittest
from .contains_duplicate import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.containsDuplicate([1, 2, 3, 1]), True)

    def test_example2(self):
        self.assertEqual(self.sol.containsDuplicate([1, 2, 3, 4]), False)

    def test_example3(self):
        self.assertEqual(self.sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
