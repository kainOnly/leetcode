import unittest
from .summary_ranges import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.summaryRanges([0, 1, 2, 4, 5, 7]), ["0->2", "4->5", "7"])
