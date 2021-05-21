import unittest
from .plus_one import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.plusOne([1, 2, 3]), [1, 2, 4])

    def test_example2(self):
        self.assertEqual(self.sol.plusOne([0]), [1])
