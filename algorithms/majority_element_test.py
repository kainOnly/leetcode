import unittest
from .majority_element import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.majorityElement([3, 2, 3]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
