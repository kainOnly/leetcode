import unittest
from .pascals_triangle_ii import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.getRow(3), [1, 3, 3, 1])
