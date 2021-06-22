import unittest
from .best_time_to_buy_and_sell_stock_ii import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_example2(self):
        self.assertEqual(self.sol.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_example3(self):
        self.assertEqual(self.sol.maxProfit([7, 6, 4, 3, 1]), 0)
