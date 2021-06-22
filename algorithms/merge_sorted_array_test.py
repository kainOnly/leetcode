import unittest
from .merge_sorted_array import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        num1 = [1, 2, 3, 0, 0, 0]
        num2 = [2, 5, 6]
        self.sol.merge(num1, 3, num2, 3)
        self.assertEqual(num1, [1, 2, 2, 3, 5, 6])

    def test_example2(self):
        num1 = [1]
        num2 = []
        self.sol.merge(num1, 1, num2, 0)
        self.assertEqual(num1, [1])
