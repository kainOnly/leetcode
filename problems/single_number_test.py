import unittest
from .single_number import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.singleNumber([2, 2, 1]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.singleNumber([4, 1, 2, 1, 2]), 4)
