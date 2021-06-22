import unittest
from .climbing_stairs import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.climbStairs(2), 2)

    def test_example2(self):
        self.assertEqual(self.sol.climbStairs(3), 3)

    def test_example3(self):
        self.assertEqual(self.sol.climbStairs(4), 5)
