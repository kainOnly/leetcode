import unittest
from .maximum_subarray import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
