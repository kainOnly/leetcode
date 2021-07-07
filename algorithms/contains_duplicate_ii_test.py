import unittest
from .contains_duplicate_ii import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 3), True)

    def test_example2(self):
        self.assertEqual(self.sol.containsNearbyDuplicate([1, 0, 1, 1], 1), True)

    def test_example3(self):
        self.assertEqual(self.sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)

    def test_example4(self):
        self.assertEqual(self.sol.containsNearbyDuplicate([99, 99], 2), True)
