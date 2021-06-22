import unittest
from .two_sum_ii_input_array_is_sorted import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [1, 2])
